from typing import Literal

from pydantic import BaseModel


class Content(BaseModel):
    full: str
    summary: str


class Attitude(BaseModel):
    citation: list[str]
    attitude: Literal["positive", "neutral", "negative"]


class ClassifyOutput(BaseModel):
    content: Content | None = None
    attitudes: dict[Literal["china", "taiwan", "hongkong", "usa"], Attitude | None] | None
    emotion: Literal[-2, -1, 0, 1, 2]
