from fastapi import APIRouter

router = APIRouter(
    prefix="/players",
    tags=["players"]
)

@router.get("/")
def list_players():
    return []
