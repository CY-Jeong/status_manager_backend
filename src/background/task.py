from fastapi import BackgroundTasks, Depends

import logging
import asyncio

from src.services.status_service import StatusService
from src.dtos.status_dto import SystemStatusOutDto
from src.models.base_model import JsonModel
from src.repo.base_repo import insert_one

logger = logging.getLogger(__name__)

async def put_db(status_service: StatusService = Depends(StatusService)):
    while True:
        logger.info("put status")
        ret = await status_service.get_node_status()
        out_dto = SystemStatusOutDto(**ret.dict())
        #status_json = JsonModel.to_camel(out_dto.dict())
        await insert_one(out_dto.dict())
        asyncio.sleep(10)

def put_status_db(background_tasks: BackgroundTasks):
    background_tasks.add_task(put_db)
    return "start saving info"
