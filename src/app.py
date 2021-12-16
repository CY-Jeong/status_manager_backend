from typing import Optional
import os
import logging
import logging.config
from dotenv import load_dotenv

load_dotenv(dotenv_path=f".{os.getenv('DOT_ENV', 'development')}.env")

from pathlib import Path
from src.router.status_router import router as status_router
from src.router.index_router import router as index_router
from src.security.authenticate import validate_api_key
from src.background.task import put_status_db
from src.database.mongodb import connect_mongo, disconnect_mongo

from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials


logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

logger.info(os.environ)


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Boilerplate",
        description="desrciption",
        version="1.0.0",
        openapi_url="/docs/openapi.json",
    )
    return app


app = create_app()
app.include_router(
    index_router,
    prefix="/api",
    dependencies=[Security(validate_api_key, scopes=["openid"])],
)
app.include_router(
    status_router,
    prefix="/api/status",
    dependencies=[Security(validate_api_key, scopes=["openid"])],
)


@app.on_event("startup")
async def on_app_start(q: str = Depends(put_status_db)):
    logger.info("App initalize")
    mongo_conn_url = os.getenv("MONGO_CONNECTION_URL")

    if mongo_conn_url:
        await connect_mongo(mongo_conn_url)
    logger.info(q)
    


@app.on_event("shutdown")
async def on_app_shutdown():
    await disconnect_mongo()