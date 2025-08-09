from app.services.expense_service import create_expense, get_all_expenses

def test_create_and_read():
    create_expense("Teszt kategória", 1234.56, "Teszt megjegyzés")
    expenses = get_all_expenses()
    assert len(expenses) > 0
    assert expenses[-1].category == "Teszt kategória"
