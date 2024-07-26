import flet as ft

def main(page: ft):

    def login(e):
        
        if not entradaNome.value:
            entradaNome.error_text = "Por favor preencha seu nome!"
            page.update()
        if not entradaSenha.value:
            entradaSenha.error_text = "Campo de senha obrogatorio!"
            page.update()   
        else:   
            nome = entradaNome.value
            senha = entradaSenha.value

            print(f"Nome: {nome}\nSenha: {senha}")

            page.clean()
            page.add(ft.Text(f"Ola, {nome}\nSeja bem vindo(a) a nossa aplcação."))
            page.update()

        pass
    
    entradaNome = ft.TextField(label="Insira seu nome")
    entradaSenha = ft.TextField(label="Insira sua senha")

    page.add(
        entradaNome,
        entradaSenha,
        ft.ElevatedButton(text="Entrar", on_click=login)
    )

    pass



ft.app(target=main)