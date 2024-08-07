from app.endpoints.endpoints import router
from app.settings.app_factory import get_app

app = get_app()

app.include_router(router)
