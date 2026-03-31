# import flet as ft

# def main_page(page: ft.Page):
#     page.title = 'My first app'
#     page.theme_mode =ft.ThemeMode.LIGHT


#     text_hello=ft.Text('hello world')

#     elevated_buttom =ft.ElevatedButton('send',icon=ft.Icons.SEND,color=ft.Colors.BLACK,icon_color=ft.Colors.GREEN)
#     text_button =ft.TextButton('send')
#     icon_button = ft.IconButton(icon=ft.Icons.SEND)


#     page.add(text_hello,elevated_buttom,text_button,icon_button)

# ft.app(main_page)


import flet as ft

def main_page(page: ft.Page):
    page.title = 'Счётчик'
    page.theme_mode = ft.ThemeMode.SYSTEM

    count = 0  

    text_hello = ft.Text('Нажато: 0 раз', size=40)

    def on_click(e):
        nonlocal count
        count += 1
        text_hello.value = f'Нажато: {count} раз'
        page.update()  

    def on_reset(e):
        nonlocal count
        count = 0
        text_hello.value = 'Нажато: 0 раз'
        page.update()

    button = ft.ElevatedButton(
        'Нажми меня',
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.PURPLE,
        on_click=on_click
    )

    reset_button = ft.TextButton('сбросить', on_click=on_reset)

    page.add(text_hello, button, reset_button)

ft.app(main_page)