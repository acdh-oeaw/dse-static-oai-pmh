# dse-static-oai-pmh
OAI-PMH proxy server for dse-static based digital editions, implemented with [FastAPI](https://fastapi.tiangolo.com/)

## install and run

```
git clone https://github.com/acdh-oeaw/dse-static-oai-pmh.git
cd dse-static-oai-pmh
pip install -r requirements.txt
./startserver
```

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