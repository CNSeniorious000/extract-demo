from typing import Literal

from pydantic import BaseModel


class Attitude(BaseModel):
    attitude: Literal["positive", "neutral", "negative"]
    entity: str
    text: str


class ExtractOutput(BaseModel):
    attitudes: list[Attitude]
