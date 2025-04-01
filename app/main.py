import datetime

import lxml.etree as ET
from fastapi import FastAPI, Request, Response, Query, HTTPException, Path
from typing import Annotated
from acdh_tei_pyutils.tei import TeiReader


from app.config import VERB_MAPPING, ENDPOINTS, FULLTEXT_BLACK_LIST

cur_date = cur_date = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
blacklist_xpath = " or ".join([f"ancestor::{tag}" for tag in FULLTEXT_BLACK_LIST])
fulltext_xpath = f"//tei:body/.//text()[not({blacklist_xpath})]"

nsmap = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
}

app = FastAPI()


@app.get("/")
async def root(request: Request):
    current_url = str(request.base_url)
    endpoints = {}
    for key, value in ENDPOINTS.items():
        endpoints[key] = value.copy()
        endpoints[key]["oai"] = f"{current_url}{key}/oai-pmh"
        try:
            endpoints[key]["fulltext_xpath"]
        except KeyError:
            endpoints[key]["fulltext_xpath"] = fulltext_xpath
    return {
        "docs": f"{current_url}docs",
        "code-repo": "https://github.com/acdh-oeaw/dse-static-oai-pmh",
        "endpoints": endpoints,
    }


@app.get(
    "/{project}/oai-pmh",
    responses={
        200: {
            "content": {"application/xml": {}},
            "description": "Return the OAI-PMH XML response",
        }
    },
)
@app.post(
    "/{project}/oai-pmh",
    responses={
        200: {
            "content": {"application/xml": {}},
            "description": "Return the OAI-PMH XML response",
        }
    },
)
async def oai_pmh_endpoint(
    request: Request,
    project: Annotated[str, Path(enum=list(ENDPOINTS.keys()))],
    # GET parameters
    verb: Annotated[str | None, Query(enum=list(VERB_MAPPING.keys()))] = None,
    identifier: Annotated[str | None, Query()] = None,
    metadataPrefix: Annotated[str | None, Query()] = None,
    from_: Annotated[str | None, Query(alias="from")] = None,
    until: Annotated[str | None, Query()] = None,
    set: Annotated[str | None, Query()] = None,
    resumptionToken: Annotated[str | None, Query()] = None,
):
    """Handles OAI-PMH GET and POST requests for specified projects.
    Returns XML response in OAI-PMH format.
    """
    params = {}
    if request.method == "POST":
        form_data = await request.form()
        params = dict(form_data)
        used_verb = params.get("verb")
    else:
        # GET request - collect query parameters
        used_verb = verb
        if identifier:
            params["identifier"] = identifier
        if metadataPrefix:
            params["metadataPrefix"] = metadataPrefix
        if from_:
            params["from"] = from_
        if until:
            params["until"] = until
        if set:
            params["set"] = set
        if resumptionToken:
            params["resumptionToken"] = resumptionToken
    params["verb"] = used_verb

    if not used_verb:
        return Response(
            content="Missing OAI-PMH verb",
            status_code=400,
            media_type="text/plain;charset=UTF-8",
        )

    if used_verb not in VERB_MAPPING:
        return Response(
            content="Invalid OAI-PMH verb",
            status_code=400,
            media_type="text/plain;charset=UTF-8",
        )

    try:
        project_object = ENDPOINTS[project]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Project {project} not found")

    base_url = project_object["url"]
    if used_verb == "GetRecord" and identifier:
        full_url = f'{base_url}{VERB_MAPPING["ListRecords"]}'
    elif used_verb == "GetRecord":
        return Response(
            content="The value of the identifier argument is unknown or illegal in this repository.",
            status_code=400,
            media_type="text/plain;charset=UTF-8",
        )
    else:
        full_url = f"{base_url}{VERB_MAPPING[used_verb]}"
    doc = TeiReader(full_url)
    try:
        default_lang = ENDPOINTS[project]["default_lang"]
    except KeyError:
        default_lang = False
    if default_lang:
        for x in doc.tree.xpath(".//oai_dc:dc[not(./dc:language)]", namespaces=nsmap):
            element = ET.Element("{http://purl.org/dc/elements/1.1/}language")
            element.text = default_lang
            x.append(element)

    for x in doc.tree.xpath(".//oai:responseDate", namespaces=nsmap):
        x.text = cur_date
    for x in doc.tree.xpath(".//oai:request", namespaces=nsmap):
        for key, value in params.items():
            x.attrib[key] = value
    if used_verb == "GetRecord" and identifier:
        try:
            record = doc.tree.xpath(
                f".//oai:record[./oai:header/oai:identifier='{identifier}']",
                namespaces=nsmap,
            )[0]
        except IndexError:
            return Response(
                content="The value of the identifier argument is unknown or illegal in this repository.",
                status_code=400,
                media_type="text/plain;charset=UTF-8",
            )
        for bad in doc.tree.xpath(".//oai:ListRecords", namespaces=nsmap):
            bad.getparent().remove(bad)
        get_record = ET.Element("{http://www.openarchives.org/OAI/2.0/}GetRecord")
        root = doc.tree.xpath("/oai:OAI-PMH", namespaces=nsmap)[0]
        root.append(get_record)
        get_record.append(record)
    return Response(content=doc.return_string(), media_type="application/xml")
