from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from viewmodels.receipt_viewmodel import ReceiptViewModel
from database import get_db
from schemas.receipt_schema import ReceiptCreate, ReceiptResponse
router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)


@router.post("/", response_model=ReceiptResponse)
def create_receipt(receipt_data:ReceiptCreate, db: Session = Depends(get_db)):
    receipt_vm=ReceiptViewModel(db)
    return receipt_vm.create_receipt(receipt_data,user_id=1)
