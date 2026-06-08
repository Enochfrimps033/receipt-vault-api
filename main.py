from fastapi import FastAPI

from database import engine, Base
from routes import users, receipts

from models.user_model import User
from models.receipt_model import Receipt

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Receipt Vault API")

app.include_router(users.router)
app.include_router(receipts.router)
for route in app.routes:
    print(route.path, route.methods)
@app.get("/")
def root():
    return {"message": "Receipt Vault API is running"}