from promptools.extractors import extract_json

from .templates import prompt_template
from .utils.llm import complete
from .utils.schema import Output


def extract(topic: str, content: str):
    prompt = prompt_template.render({"topic": topic, "content": content})
    result = complete(prompt)
    output = extract_json(result, expect=Output)
    return output
