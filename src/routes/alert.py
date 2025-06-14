from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated

# from src.authentication_manager import get_current_user
from src.database.database import get_db
from src.database.models import User
from src.response_manager import ResponseManager

router = APIRouter()

# class AlertResponse(BaseModel):
#     user_id: int
#     username: str
#     budget: float
#     total_expenses: float
#     alert: str

# @router.get("/", responses=ResponseManager.responses, name="Get Alerts")
# async def get_alerts(
#     db: Annotated[Session, Depends(get_db)],
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     users = db.query(User).all()
#     alerts = []
#     for user in users:
#         total_expenses = sum(expense.amount for expense in user.expenses)
#         if total_expenses > user.budget:
#             alerts.append(AlertResponse(
#                 user_id=user.id,
#                 username=user.username,
#                 budget=user.budget,
#                 total_expenses=total_expenses,
#                 alert="Budget exceeded!"
#             ))
#     return alerts