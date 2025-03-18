from fastapi import FastAPI, Request, Response, Query, HTTPException, Path
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
    return {"endpoints": endpoints}


@app.get(
    "/{project}/oai-pmh",
    responses={
        200: {
            "content": {"application/xml": {}},
            "description": "Return the OAI-PMH XML response"
        }
    }
)
async def oai_pmh_get(
    project: Annotated[str, Path(enum=list(ENDPOINTS.keys()))],
    verb: str = Query(None, enum=list(VERB_MAPPING.keys()))
):
    """Handles OAI-PMH GET requests for specified projects.
    Returns XML response in OAI-PMH format.
    """
    if verb not in VERB_MAPPING:
        return Response(content="Invalid or missing OAI-PMH verb", status_code=400)
    try:
        project_object = ENDPOINTS[project]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Project {project_object} not found")
    base_url = project_object["url"]
    full_url = f"{base_url}{VERB_MAPPING[verb]}"
    doc = TeiReader(full_url)
    return Response(content=doc.return_string(), media_type="application/xml")
