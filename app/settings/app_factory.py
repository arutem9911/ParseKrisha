import functools

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status
from loguru import logger

from app.schema.response_body import ParsedData, ParsingStage


class AppFactory:
    def __init__(self):
        self.app = FastAPI()

        @self.app.on_event("startup")
        async def start_up():
            logger.info("Async session started!!!")

        @self.app.on_event("shutdown")
        async def shutdown():
            logger.info("Async session has stopped!!!")

        # async def try_execute_async(func):
        #     @functools.wraps(func)
        #     async def wrapper(*args, **kwargs):
        #         print(args)
        #         return JSONResponse(
        #             status_code=status.HTTP_400_BAD_REQUEST,
        #             content=ParsedData(
        #                 stage=ParsingStage.
        #             )
        #         )


app = AppFactory()


def get_app():
    return app.app
