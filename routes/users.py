from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/test")
def test_auth_route():
    return {"message": "Auth route is working"}