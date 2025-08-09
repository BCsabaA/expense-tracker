import flet as ft
from app.main import main

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")
