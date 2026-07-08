from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from database import get_db
from schemas.receipt_schema import ReceiptCreate, ReceiptResponse
from viewmodels.receipt_viewmodel import ReceiptViewModel
from services.openai_service import extract_receipt_data
# this is a mini  Fastapi class(APIRouter)
router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)


@router.post("/", response_model=ReceiptResponse)
def create_receipt(receipt_data:ReceiptCreate, db: Session = Depends(get_db)):
    receipt_vm=ReceiptViewModel(db)
    return receipt_vm.create_receipt(receipt_data,user_id=1)
    
@router.post("/scan",response_model=ReceiptResponse)
async def scan_receipt(file: UploadFile = File(...), db: Session=Depends(get_db)):
    image_bytes = await file.read()
    #passing the image itself and the type of image file)
    result = extract_receipt_data(image_bytes,file.content_type)
    receipt_data= ReceiptCreate(**result)#validates the input data before saving/ "**" unpacks dict into keyword args. so ReceiptCreate but with the filled in data
    receipt_vm = ReceiptViewModel(db)
    saved_receipt = receipt_vm.create_receipt(receipt_data, user_id=1)

    return saved_receipt