from fastapi import FastAPI, Request, Response, Query, HTTPException, Path, Form
from typing import Annotated
from acdh_tei_pyutils.tei import TeiReader

from app.config import VERB_MAPPING
from app.config import ENDPOINTS

app = FastAPI()


@app.get("/")
async def root(request: Request):
    current_url = str(request.base_url)
    endpoints = {}
    for key, value in ENDPOINTS.items():
        endpoints[key] = value.copy()
        endpoints[key]["oai"] = f"{current_url}{key}/oai-pmh"
    return {"docs": f"{current_url}docs", "endpoints": endpoints}


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

    if not used_verb:
        return Response(
            content="Missing OAI-PMH verb",
            status_code=400,
            media_type="application/xml"
        )

    if used_verb not in VERB_MAPPING:
        return Response(
            content="Invalid OAI-PMH verb",
            status_code=400,
            media_type="application/xml"
        )

    try:
        project_object = ENDPOINTS[project]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Project {project} not found"
        )

    base_url = project_object["url"]
    full_url = f"{base_url}{VERB_MAPPING[used_verb]}"
    doc = TeiReader(full_url)
    return Response(content=doc.return_string(), media_type="application/xml")
