from models.receipt_model import Receipt
from sqlalchemy.orm import Session
from schemas.receipt_schema import ReceiptCreate

class ReceiptViewModel:
    def __init__(self, db:Session):
        self.db = db

    def create_receipt(self, receipt_data: ReceiptCreate,user_id:int ):
        new_receipt=Receipt(
            user_id=user_id,
            store_name = receipt_data.store_name,
            amount = receipt_data.amount,
            date = receipt_data.date,
            return_window = receipt_data.return_window,
            warranty_until = receipt_data.warranty_until,
            warranty_info = receipt_data.warranty_info,
            image_url = receipt_data.image_url
                    
        )

        self.db.add(new_receipt)
        self.db.commit()
        self.db.refresh(new_receipt)

        return new_receipt
    def get_receipts(self):
        all_receipts = self.db.query(Receipt).all()
        return all_receipts