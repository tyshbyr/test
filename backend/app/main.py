from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.api.v1.users import router as users_router
from app.config.project_config import app_config

app = FastAPI(
    title=app_config.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(users_router, prefix="/users", tags=["users"])
