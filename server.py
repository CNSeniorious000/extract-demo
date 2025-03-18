from json import loads

from fastapi import Body, FastAPI, HTTPException
from pydantic import ValidationError

from src.api import ClassifyOutput, ExtractOutput, Model, classify, extract

app = FastAPI(title="Extractor API")


@app.post("/classify")
def classification(
    include_full_content: bool = False,
    article: str = Body(media_type="text/plain"),
    llm: Model = "gpt-4o",
) -> ClassifyOutput:
    try:
        return classify(article, include_full_content, llm)
    except ValidationError as e:
        raise HTTPException(500, loads(e.json(include_input=False))) from e


@app.post("/extract")
def extraction(
    topic: str,
    content: str = Body(media_type="text/plain"),
    llm: Model = "gpt-4o-mini",
) -> ExtractOutput:
    try:
        return extract(topic, content, llm)
    except ValidationError as e:
        raise HTTPException(500, loads(e.json(include_input=False))) from e
