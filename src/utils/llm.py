from dotenv import load_dotenv
from promplate.llm.openai import ChatGenerate

load_dotenv(override=True)

generate = ChatGenerate().bind(
    model="gpt-4o",  # most efficiency
    response_format={"type": "json_object"},  # for structural output
    temperature=0,
)


def complete(messages, **kwargs):
    res = ""

    for i in generate(messages, **kwargs):
        res += i
        print(i, end="", flush=True)
    print()

    return res
