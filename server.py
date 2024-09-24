from fastapi import Body, FastAPI

from src.api import Output, extract

app = FastAPI(title="Extractor API")


@app.post("/extract")
def extract_data(topic: str, content: str = Body(media_type="text/plain")) -> Output | None:
    return extract(topic, content)
