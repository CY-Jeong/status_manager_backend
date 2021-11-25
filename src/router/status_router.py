from fastapi import APIRouter

router = APIRouter(
    tags=["status"],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}}
)

@router.get(
    ""
)