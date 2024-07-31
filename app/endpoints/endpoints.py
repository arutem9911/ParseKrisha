from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/check_availability/")
async def check_availability():
    return {"status": "Available"}
