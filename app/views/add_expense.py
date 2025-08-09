import flet as ft
from app.services.expense_service import create_expense

def add_expense_view(page: ft.Page):
    page.title = "Új költés"

    category = ft.TextField(label="Kategória")
    amount = ft.TextField(label="Összeg (Ft)", keyboard_type=ft.KeyboardType.NUMBER)
    description = ft.TextField(label="Megjegyzés", multiline=True)

    def save_expense(e):
        try:
            create_expense(category.value, float(amount.value), description.value)
            page.snack_bar = ft.SnackBar(ft.Text("Költés mentve!"))
            page.snack_bar.open = True
            page.go("/expenses")
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Hiba: {ex}"))
            page.snack_bar.open = True
            page.update()

    page.add(
        category,
        amount,
        description,
        ft.ElevatedButton("Mentés", on_click=save_expense),
        ft.ElevatedButton("Vissza", on_click=lambda e: page.go("/"))
    )
