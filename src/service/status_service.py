class StatusService:
    async def check_alive(self, id: int):
        return StatusModel(id=id, os=" ubuntu ", gpu_status=False)