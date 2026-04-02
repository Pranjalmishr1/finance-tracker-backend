from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app import models
from app.utils.permissions import role_required

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Total Income
@router.get("/analytics/income")
def total_income(db: Session = Depends(get_db)):
    income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "income"
    ).scalar()

    return {"total_income": income or 0}


# Total Expense
@router.get("/analytics/expense")
def total_expense(db: Session = Depends(get_db)):
    expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "expense"
    ).scalar()

    return {"total_expense": expense or 0}


# Current Balance
@router.get("/analytics/balance")
def current_balance(db: Session = Depends(get_db)):

    income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "income"
    ).scalar() or 0

    expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.type == "expense"
    ).scalar() or 0

    return {"current_balance": income - expense}
from sqlalchemy import extract


# Category-wise breakdown
@router.get("/analytics/category-breakdown")
def category_breakdown(db: Session = Depends(get_db)):

    results = db.query(
        models.Transaction.category,
        func.sum(models.Transaction.amount)
    ).group_by(models.Transaction.category).all()

    breakdown = {
        category: total for category, total in results
    }

    return {"category_breakdown": breakdown}
# Monthly totals
@router.get("/analytics/monthly-summary")
def monthly_summary(db: Session = Depends(get_db)):

    results = db.query(
        extract("month", models.Transaction.date),
        func.sum(models.Transaction.amount)
    ).group_by(
        extract("month", models.Transaction.date)
    ).all()

    summary = {
        int(month): total for month, total in results
    }

    return {"monthly_summary": summary}
# Recent activity (last 5 transactions)
@router.get("/analytics/recent-activity")
def recent_activity(db: Session = Depends(get_db)):

    transactions = db.query(models.Transaction)\
        .order_by(models.Transaction.date.desc())\
        .limit(5)\
        .all()

    return {"recent_activity": transactions}