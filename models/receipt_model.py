from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True,index=True)
    #foriegnkey connect one table to another. In other words another tables primary key
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    store_name = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    date = Column(String, nullable=True)
    return_window = Column(String,nullable=True)
    warranty_until = Column(String,  nullable=True)
    warranty_info = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    owner = relationship("User", back_populates="receipts")