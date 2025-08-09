import flet as ft
from app.services.expense_service import get_all_expenses

def expense_list_view(page: ft.Page):
    page.title = "Költések"
    data = get_all_expenses()

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Dátum")),
            ft.DataColumn(ft.Text("Kategória")),
            ft.DataColumn(ft.Text("Összeg")),
            ft.DataColumn(ft.Text("Megjegyzés"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(e.date))),
                    ft.DataCell(ft.Text(e.category)),
                    ft.DataCell(ft.Text(f"{e.amount} Ft")),
                    ft.DataCell(ft.Text(e.description or ""))
                ]
            )
            for e in data
        ]
    )

    page.add(
        ft.Text("Költések listája", size=20),
        table,
        ft.ElevatedButton("Vissza", on_click=lambda e: page.go("/"))
    )
