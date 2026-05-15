from fastapi import APIRouter

router = APIRouter(
    prefix="/teams",
    tags=["teams"]
)

@router.get("/")
def list_teams():
    return []

@router.post("/")
def create_team():
    return {"message": "Team created successfully"}