from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import transactions, analytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker Backend API")

app.include_router(transactions.router)
app.include_router(analytics.router)


@app.get("/")
def home():
    return {"message": "Finance Backend Running Successfully 🚀"}