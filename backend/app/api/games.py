from fastapi import APIRouter

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/")
def list_games():
    return []
