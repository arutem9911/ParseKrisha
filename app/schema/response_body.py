from pydantic import BaseModel
from enum import Enum


class TaskIdResponse(BaseModel):
    task_id: str
    status: str = "Parsing has started!"


class ParsingStage(Enum, str):
    collect_advert_id: "collect_advert_id"
    parsing: "parsing"


class ParsedData(BaseModel):
    task_id: str
    stage: ParsingStage
    status: str = "in progress"
    result: list = []
