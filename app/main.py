from fastapi import FastAPI, Request, Response, Query, HTTPException, Path
from typing import Annotated


from app.config import VERB_MAPPING
from app.config import ENDPOINTS

app = FastAPI()


verbs = [
    "Identify",
    "ListMetadataFormats",
]


@app.get("/")
async def root(request: Request):
    return {"foo": "bar"}


@app.get("/{project}/oai-pmh")
async def oai_pmh_get(
    project: Annotated[str, Path(enum=list(ENDPOINTS.keys()))],
    verb: str = Query(None, enum=verbs)
):
    """Handles OAI-PMH GET requests for specified projects.
    """
    if verb not in VERB_MAPPING:
        return Response(content="Invalid or missing OAI-PMH verb", status_code=400)
    try:
        project_object = ENDPOINTS[project]
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"project": project_object, "verb": verb}
