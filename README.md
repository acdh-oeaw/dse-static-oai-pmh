[![Test](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/test.yml)
[![Lint](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/lint.yml)
[![Build and publish Docker image](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/build.yml/badge.svg)](https://github.com/acdh-oeaw/dse-static-oai-pmh/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/dse-static-oai-pmh/graph/badge.svg?token=zWVEoXKCFy)](https://codecov.io/gh/acdh-oeaw/dse-static-oai-pmh)

# dse-static-oai-pmh

OAI-PMH proxy server for dse-static based digital editions, implemented with [FastAPI](https://fastapi.tiangolo.com/)

## install and run

```shell
git clone https://github.com/acdh-oeaw/dse-static-oai-pmh.git
cd dse-static-oai-pmh
uv run fastapi dev
```

### tests

```shell
uv run coverage run -m pytest -v
``

## config
Register new dse-static-editions by configuring `ENDPOINTS` in [app/config.py](app/config.py).

### list endpoints
```shell
curl "http://localhost:8000"
```

### docs endpoints
```shell
curl "http://localhost:8000/docs"
```

### GET request
```shell
curl "http://localhost:8000/{project}/oai-pmh?verb=Identify"
curl "http://localhost:8000/tillich-lectures/oai-pmh?verb=Identify"
```

### POST request
```shell
curl -X POST -d "verb=Identify" "http://localhost:8000/{project}/oai-pmh"
curl -X POST -d "verb=Identify" "http://localhost:8000/tillich-lectures/oai-pmh"
```

### Docker

```shell
docker build -t dse-oai-pmh .
docker run -d --rm --name dse-oai-pmh  -p 8020:8020 dse-oai-pmh
```