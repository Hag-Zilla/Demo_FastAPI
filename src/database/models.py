from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.database.database import Base
from datetime import date

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    budget = Column(Float)
    role = Column(String, default="user")  # Default role is "user"
    disabled = Column(Boolean, default=False)  # Indicates if the user account is disabled
    expenses = relationship("Expense", back_populates="owner")

# Expense model
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    date = Column(Date, default=date.today)
    category = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="expenses")