from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse(os.path.join("static", "index.html"))

# In-memory user and merchant data
users = {
    "HAND123": {"pin": "1234", "upi": "user@upi", "balance": 1000.0},
}
merchants = {
    "merchant001": {"upi": "merchant@upi", "balance": 500.0},
}

class PaymentRequest(BaseModel):
    hand_id: str
    pin: str
    amount: float

@app.post("/pay/{merchant_id}")
def pay(merchant_id: str, req: PaymentRequest):
    user = users.get(req.hand_id)
    merchant = merchants.get(merchant_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user["pin"] != req.pin:
        raise HTTPException(status_code=401, detail="Invalid PIN")
    if user["balance"] < req.amount:
        raise HTTPException(status_code=402, detail="Insufficient funds")
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")

    # Simulate UPI transfer
    user["balance"] -= req.amount
    merchant["balance"] += req.amount

    return {
        "status": "success",
        "from": user["upi"],
        "to": merchant["upi"],
        "amount": req.amount
    }
