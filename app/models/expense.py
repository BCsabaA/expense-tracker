from sqlalchemy import Column, Integer, String, Float, Date
from app.models.database import Base
from datetime import date

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
