import time
import flet as ft
import threading

def main(page: ft.Page):

    lock = threading.Lock()

    def reveal(event):
        page.update()

    page.add(ft.ElevatedButton("Revelar", on_click=reveal))

    page.scroll = "always"

    def count_lines():
        i = 1
        while True:
            with lock:
                page.controls.append(ft.Text(f"Estamos na linha: {i}"))
                time.sleep(1)
                i += 1

    threading.Thread(target=count_lines, daemon=True).start()

ft.app(target=main, view=ft.WEB_BROWSER)