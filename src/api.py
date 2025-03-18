from contextlib import suppress
from typing import Literal

from promptools.extractors import find_json_blocks

from .templates import classify_template, extract_template
from .utils.llm import complete
from .utils.schema.classify import ClassifyOutput
from .utils.schema.extract import ExtractOutput

type Model = Literal["gpt-4o", "gpt-4o-mini", "llama-3.3-70b", "grok-2-1212", "qwen-qwq-32b"]


def classify(article: str, need_content: bool, llm: Model):
    prompt = classify_template.render({"article": article, "content": need_content})
    result = complete(prompt, model=llm)
    with suppress(IndexError):
        result = find_json_blocks(result)[-1]
    return ClassifyOutput.model_validate_json(result)


def extract(topic: str, content: str, llm: Model):
    prompt = extract_template.render({"topic": topic, "content": content})
    result = complete(prompt, model=llm)
    return ExtractOutput.model_validate_json(result)
