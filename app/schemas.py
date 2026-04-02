from pydantic import BaseModel
from datetime import date


class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str


class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        orm_mode = True