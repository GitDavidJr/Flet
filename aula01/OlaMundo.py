import flet

def main(page: flet.page):

    ola = flet.Text(value="Ola mundo")
    page.controls.append(ola)
    page.update()

    pass

flet.app(target=main)