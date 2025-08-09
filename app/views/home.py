import flet as ft

def home_view(page: ft.Page):
    page.title = "Költésfigyelő"
    page.add(
        ft.Text("Üdv a Költésfigyelőben!", size=24),
        ft.ElevatedButton("Költések listája", on_click=lambda e: page.go("/expenses")),
        ft.ElevatedButton("Új költés rögzítése", on_click=lambda e: page.go("/add"))
    )
