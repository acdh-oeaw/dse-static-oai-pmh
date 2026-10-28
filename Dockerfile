FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml

COPY ./app /code/app

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8020"]
