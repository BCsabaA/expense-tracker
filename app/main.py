import flet as ft
from app.views.home import home_view
from app.views.expense_list import expense_list_view
from app.views.add_expense import add_expense_view
from app.models.database import init_db

def main(page: ft.Page):
    init_db()  # DB inicializálás induláskor

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            home_view(page)
        elif page.route == "/expenses":
            expense_list_view(page)
        elif page.route == "/add":
            add_expense_view(page)
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
