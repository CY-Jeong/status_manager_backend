from fastapi import APIRouter

router = APIRouter(
    prefix="/",
    tags=["index"],
    responses={200: {"description": "OK"}}
)s

@router.get("/")
async def index() -> dict:
    return {"status_index": True}