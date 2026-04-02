from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import SessionLocal
from app import models, schemas

router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ===============================
# CREATE TRANSACTION
# ===============================
@router.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(get_db)
):

    db_transaction = models.Transaction(**transaction.dict())

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


# ===============================
# GET ALL TRANSACTIONS
# ===============================
@router.get("/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):

    transactions = db.query(models.Transaction).all()

    return transactions


# ===============================
# FILTER TRANSACTIONS  ✅ MUST COME BEFORE ID ROUTE
# ===============================
@router.get(
    "/transactions/filter-transactions",
    response_model=list[schemas.TransactionResponse]
)
def filter_transactions(
    type: Optional[str] = None,
    category: Optional[str] = None,
    transaction_date: Optional[date] = None,
    db: Session = Depends(get_db)
):

    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)

    if category:
        query = query.filter(models.Transaction.category == category)

    if transaction_date:
        query = query.filter(models.Transaction.date == transaction_date)

    return query.all()


# ===============================
# GET SINGLE TRANSACTION
# ===============================
@router.get(
    "/transactions/{transaction_id}",
    response_model=schemas.TransactionResponse
)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


# ===============================
# UPDATE TRANSACTION
# ===============================
@router.put(
    "/transactions/{transaction_id}",
    response_model=schemas.TransactionResponse
)
def update_transaction(
    transaction_id: int,
    updated_data: schemas.TransactionCreate,
    db: Session = Depends(get_db)
):

    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    transaction.amount = updated_data.amount
    transaction.type = updated_data.type
    transaction.category = updated_data.category
    transaction.date = updated_data.date
    transaction.notes = updated_data.notes

    db.commit()
    db.refresh(transaction)

    return transaction


# ===============================
# DELETE TRANSACTION
# ===============================
@router.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.utils.permissions import role_required

router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Transaction (ADMIN only)
@router.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate,
    role: str = Depends(role_required(["admin"])),
    db: Session = Depends(get_db)
):
    db_transaction = models.Transaction(**transaction.dict())

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction