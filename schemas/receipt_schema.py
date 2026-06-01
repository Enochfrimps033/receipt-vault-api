from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReceiptCreate(BaseModel):
    store_name: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    return_window: Optional[str] = None
    warranty_until: Optional[str] = None
    warranty_info: Optional[str] = None
    image_url: Optional[str] = None


class ReceiptResponse(BaseModel):
    id: int
    user_id: int
    store_name: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    return_window: Optional[str] = None
    warranty_until: Optional[str] = None
    warranty_info: Optional[str] = None
    image_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True