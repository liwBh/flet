import flet as ft
from config.settings import app_color, app_size
from logic.logic_home import AppState


def section_header():
    text_word = ft.Text(AppState.get_word_hashed(), size=20, color=app_color["white"])
    text_attemp = ft.Text(f"❤️  {AppState.get_current_attempt()} ", size=20, color=app_color["white"])

    items = [
        ft.Container(content=text_word, width=300, height=100),
        ft.Container(content=text_attemp, width=100, height=100),
    ]
    header = ft.Container(
        width=400,
        height=60,
        content=ft.Row(controls=items, expand=False),
        margin=ft.margin.only(top=10),
        alignment=ft.alignment.center,
        expand=False,
    )

    return header, text_word, text_attemp


def section_main():
    image = ft.Image(
        src=AppState.get_image(),
        # expand=False,
        # fit=ft.ImageFit.CONTAIN,
        width=250,
        height=220,
    )

    text_game = ft.Text("", size=14, color=app_color["danger"])

    main = ft.Container(
        content=ft.Column(
            controls=[image, text_game],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        ),
        width=400,
        height=300,
        margin=ft.margin.only(top=10),
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
        border_radius=5,
        expand=False,
    )

    return main, image, text_game


def create_btn(letter, page, press_letter, text_word, text_attemp, text_game, image):
    def pressed(e):
        press_letter(letter, page, text_word, text_attemp, text_game, image)

    return ft.ElevatedButton(letter, on_click=pressed)


def section_footer(page, press_letter, reset_game, text_word, text_attemp, text_game, image):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    letter_btns = [create_btn(letter, page, press_letter, text_word, text_attemp, text_game, image) for letter in alphabet]
    reset_btn = ft.ElevatedButton(
        "Reset",
        on_click=lambda e: reset_game(page, text_word, text_attemp, text_game, image)
    )
    row_btns = ft.Row( controls=letter_btns + [reset_btn], expand=False, spacing=5, wrap=True)

    footer = ft.Container(
        width=400,
        height=240,
        content=row_btns,
        # content=ft.Row(
        #     wrap=True,
        #     spacing=5,
        #     controls=letter_btns,
        #     expand=False),
        margin=ft.margin.only(top=20),
        alignment=ft.alignment.center,
        expand=False,
    )

    return footer


def init_page(page, press_letter, reset_game):
    header, text_word, text_attemp = section_header()
    main, image, text_game = section_main()

    layout = ft.Column(
        controls=[
            header,
            main,
            section_footer(page, press_letter, reset_game, text_word, text_attemp, text_game, image),
        ],
        expand=False,
    )

    container = ft.Container(
        width=app_size["width"],
        height=app_size["height"],
        bgcolor=app_color["black"],
        content=layout,
        alignment=ft.alignment.top_center,
        expand=True,
    )

    page.add(container)
    page.update()
