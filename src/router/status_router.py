from fastapi import APIRouter

router = APIRouter(
    tags=["status"],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}}
)

@router.get(
    "/me",
    responses={200: {"description": "ok", "model": HealthStatusOutDto}},
)
async def index(
    status_service: StatusService = Depends(StatusService),
) -> HealthStatusOutDto:
    health_status = await status_service.health_check()

    return HealthStatusOutDto(**health_status)


@router.get(
    "/gpu/{gpu_id}",
)
async def get_gpu_status(
    gpu_id: str, http_client: aiohttp.ClientSession = Depends(http_client)
):
    res = await http_client.get(
        os.path.join(os.getenv("GPU_MANAGER_1"), "status", "node"),
    )
    return await res.json()