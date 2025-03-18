#/bin/bash

docker build -t dse-oai-pmh .
docker run -d --rm --name dse-oai-pmh  -p 8020:8020 dse-oai-pmh