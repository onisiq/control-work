import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello Geeks')
    history_text = ft.Text(value='История приветствий: ')
    greeting_history = []

    def on_button_click(e):
        name = name_input.value
        if name:
            text_hello.value = 'Hello ' + name
            name_input.value = ''
            greeting_history.append(name)
            history_text.value = 'История приветствий\n' + '\n'.join(greeting_history)
        else:
            text_hello.value = 'Введите имя'
            text_hello.color = ft.Colors.RED
        page.update()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

        name_input = ft.TextField(label='Введите имя', expand=True)

        button = ft.ElevatedButton('send', on_click=on_button_click)

        theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=change_theme)

        header = ft.Row([ft.Text('Мое приложение'), theme_btn])

        row = ft.Row([name_input, button])

        page.add(header, text_hello, row, history_text)

ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)

# import flet as ft

# def main_page(page: ft.Page):
#     page.title = 'Счётчик'
#     page.theme_mode = ft.ThemeMode.SYSTEM

#     count = 0  

#     text_hello = ft.Text('Нажато: 0 раз', size=40)

#     def on_click(e):
#         nonlocal count
#         count += 1
#         text_hello.value = f'Нажато: {count} раз'
#         page.update()  

#     def on_reset(e):
#         nonlocal count
#         count = 0
#         text_hello.value = 'Нажато: 0 раз'
#         page.update()

#     button = ft.ElevatedButton(
#         'Нажми меня',
#         icon=ft.Icons.ADD,
#         icon_color=ft.Colors.PURPLE,
#         on_click=on_click
#     )

#     reset_button = ft.TextButton('сбросить', on_click=on_reset)

#     page.add(text_hello, button, reset_button)

# ft.app(main_page)

