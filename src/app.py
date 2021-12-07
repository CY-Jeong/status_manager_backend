import logging
import logging.config
import os

from src.router.status_router import router as status_router
from src.router.index_router import router as index_router
from fastapi import FastAPI

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger('status_manager')

logger.info(os.environ)

app = FastAPI(
    title="Status Manager",
    description="OS, GPU, MEM Status Manger",
    version="1.0.0",
    openapi_url="/docs/openapi.json"
)

app.include_router(
    index_router,
    prefix="/",
    dependencies=[Security()]

)
