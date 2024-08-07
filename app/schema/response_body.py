from pydantic import BaseModel
from enum import Enum


class ParsingStage(str, Enum):
    collect_advert_id = "collect_advert_id"
    parsing = "parsing"


class StatusType(str, Enum):
    in_progress = "in progress"
    completed = "completed"
    canceled = "canceled"


class ParsedData(BaseModel):
    task_id: str = ""
    stage: ParsingStage
    status: StatusType = StatusType.in_progress
    result: list = []
    errorText: str | None = None
    page_count: int
