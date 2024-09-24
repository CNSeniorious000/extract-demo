from dotenv import load_dotenv
from promplate.llm.openai import ChatComplete

load_dotenv(override=True)

complete = ChatComplete().bind(
    model="gpt-4o-mini",  # most efficiency
    response_format={"type": "json_object"},  # for structural output
    max_tokens=2000,  # avoid unexpected behavior
    temperature=0,
)
