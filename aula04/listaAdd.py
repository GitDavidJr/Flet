import time
import flet as ft

def main(page: ft.Page):
    for i in range(100):
        page.add(ft.Text(f"Estamos na linha: {i+1}"))
        time.sleep(1)
    page.scroll = "always"
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)