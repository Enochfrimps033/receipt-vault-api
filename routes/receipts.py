from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from database import get_db
from schemas.receipt_schema import ReceiptCreate, ReceiptResponse
from viewmodels.receipt_viewmodel import ReceiptViewModel
from services.openai_service import extract_receipt_data

router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)


@router.post("/", response_model=ReceiptResponse)
def create_receipt(receipt_data:ReceiptCreate, db: Session = Depends(get_db)):
    receipt_vm=ReceiptViewModel(db)
    return receipt_vm.create_receipt(receipt_data,user_id=1)
    
@router.post("/scan-test")
async def scan_receipt_test(file: UploadFile = File(...)):
    image_bytes = await file.read()

    result = extract_receipt_data(image_bytes)

    return result