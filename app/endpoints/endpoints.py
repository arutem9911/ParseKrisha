from fastapi import APIRouter, BackgroundTasks
import uuid
from app.schema.response_body import ParsedData, ParsingStage

router = APIRouter()
tasks = {}


@router.get("/check_availability/")
async def check_availability():
    return {"status": "Available"}


@router.post("/start_parsing/{page_count}", response_model=ParsedData)
async def start_parsing(page_count: int):
    response_data = ParsedData(
        task_id=str(uuid.uuid4()),
        page_count=page_count,
        stage=ParsingStage.collect_advert_id
    )
    return response_data
