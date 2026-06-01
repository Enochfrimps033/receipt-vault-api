from fastapi import APIRouter

router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)

@router.get("/test")
def test_receipts_route():
    return {"message": "Receipts route is working"}