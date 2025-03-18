FROM python:3.13-alpine

WORKDIR /application
COPY . .
RUN pip install uv --disable-pip-version-check && uv sync

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
