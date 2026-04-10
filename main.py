import flet as ft
from datetime import datetime
import random

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello Geeks')
    history_text = ft.Text(value='История приветствий: ')
    greeting_history = []

    name_input = ft.TextField(label='Введите имя', expand=True)

    history_visible = True

    def on_button_click(e):
        name = name_input.value
        if name:
            current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.value = f"{current_time} - Привет, {name}!"
            name_input.value = ''
            greeting_history.append(f"{current_time} - {name}")
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

    def random_name(e):
        names = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Анна"]
        name_input.value = random.choice(names)
        page.update()

    def toggle_history(e):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        page.update()

    button = ft.ElevatedButton('send', on_click=on_button_click)
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=change_theme)

    random_btn = ft.TextButton('Случайное имя', on_click=random_name)
    toggle_btn = ft.TextButton('Скрыть/Показать историю', on_click=toggle_history)

    header = ft.Row([ft.Text('Мое приложение'), theme_btn])
    row = ft.Row([name_input, button])
    extra_row = ft.Row([random_btn, toggle_btn])

    page.add(header, text_hello, row, extra_row, history_text)

ft.app(main_page)