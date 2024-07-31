from fastapi import FastAPI
from app.endpoints.endpoints import router


app = FastAPI()

app.include_router(router)
