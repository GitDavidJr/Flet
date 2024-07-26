import flet as ft

def app(page: ft.Page):

    def tecla(e: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla pressionada: {e.key} Ctrl: {e.ctrl} Alt: {e.alt} Shift: {e.shift} Meta: {e.meta}")
        )
    
    page.on_keyboard_event = tecla

    page.add(
        ft.Text("Precione qualquer tenha ou uma combinação com Ctrl, Alt, Shift ou Meta:")
    )

    pass
ft.app(target=app)