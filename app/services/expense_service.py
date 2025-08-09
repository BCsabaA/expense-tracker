from app.models.database import get_session
from app.models.expense import Expense
from datetime import date

def create_expense(category, amount, description=""):
    session = get_session()
    expense = Expense(
        date=date.today(),
        category=category,
        amount=amount,
        description=description
    )
    session.add(expense)
    session.commit()
    session.close()
    return expense

def get_all_expenses():
    session = get_session()
    expenses = session.query(Expense).all()
    session.close()
    return expenses
