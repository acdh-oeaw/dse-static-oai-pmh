import lxml.etree as ET
import pytest
from fastapi.testclient import TestClient

from app import main


def _parse_xml(response):
    return ET.fromstring(response.text.encode("utf-8"))


@pytest.fixture
def client():
    with TestClient(main.app) as test_client:
        yield test_client


def test_root_returns_docs_and_endpoint_metadata(client):
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["docs"] == "http://testserver/docs"
    assert "schnitzler-briefe" in payload["endpoints"]
    assert (
        payload["endpoints"]["schnitzler-briefe"]["oai"]
        == "http://testserver/schnitzler-briefe/oai-pmh"
    )


def test_for_missing_props(client):
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["docs"] == "http://testserver/docs"
    assert "hsa" in payload["endpoints"]
    assert (
        payload["endpoints"]["hsa"]["oai"]
        == "http://testserver/hsa/oai-pmh"
    )
    assert "fake" in payload["endpoints"]["hsa"]["pid"]


def test_oai_get_missing_verb_returns_400(client):
    response = client.get("/dse-static/oai-pmh")
    assert response.status_code == 400
    assert response.text == "Missing OAI-PMH verb"


def test_oai_post_invalid_verb_returns_400(client):
    response = client.post("/dse-static/oai-pmh", data={"verb": "Nope"})
    assert response.status_code == 400
    assert response.text == "Invalid OAI-PMH verb"


def test_identify_uses_real_teireader_and_returns_xml_response(client):
    response = client.get("/dse-static/oai-pmh", params={"verb": "Identify"})
    assert response.status_code == 200
    root = _parse_xml(response)
    ns = main.nsmap
    response_date = root.xpath("./oai:responseDate/text()", namespaces=ns)[0]
    assert response_date == main.cur_date
    request_node = root.xpath("./oai:request", namespaces=ns)[0]
    assert request_node.attrib["verb"] == "Identify"
    assert response.headers["content-type"].startswith("application/xml")


def test_getrecord_without_identifier_returns_400(client):
    response = client.get("/dse-static/oai-pmh", params={"verb": "GetRecord"})
    assert response.status_code == 400
    assert "identifier argument is unknown or illegal" in response.text
