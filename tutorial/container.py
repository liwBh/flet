import flet as ft
import random


def container_clickable():
    return ft.Column(
        [
            ft.Text("Containers - clickable and not"),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("Non clickable"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.AMBER,
                        width=150,
                        height=150,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Text("Clickable without Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.GREEN_200,
                        width=150,
                        height=150,
                        border_radius=10,
                        on_click=lambda e: print("Clickable without Ink clicked!"),
                    ),
                    ft.Container(
                        content=ft.Text("Clickable with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.CYAN_200,
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Clickable with Ink clicked!"),
                    ),
                    ft.Container(
                        content=ft.Text("Clickable transparent with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def change_img(e, page, img_container):
    index = random.randint(1, 1000)
    img_container.image = ft.DecorationImage(
        src=f"https://picsum.photos/250/250?random={index}"
    )
    index += 1
    page.update()


def container_blur(page):

    img_container = ft.Container(
        image=ft.DecorationImage(src="https://picsum.photos/250/250"),
        width=250,
        height=250,
    )

    stack = ft.Stack(
        [
            img_container,
            ft.Container(
                width=100,
                height=100,
                blur=10,
                bgcolor="#22CCCC00",
            ),
            ft.Container(
                width=100,
                height=100,
                left=20,
                top=120,
                blur=(0, 10),
            ),
            ft.Container(
                top=50,
                right=10,
                blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
                width=100,
                height=100,
                bgcolor="#44CCCCCC",
                border_radius=10,
                border=ft.border.all(2, ft.Colors.BLACK),
            ),
            ft.ElevatedButton(
                text="Change Background",
                bottom=5,
                right=5,
                style=ft.ButtonStyle(text_style=ft.TextStyle(size=8)),
                on_click=lambda e: change_img(e, page, img_container),
            ),
        ]
    )

    return ft.Column(
        [
            ft.Text("Containers - blur"),
            ft.Row(
                [
                    stack,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def on_hover(e):
    e.control.bgcolor = "blue" if e.data == "true" else "red"
    e.control.update()

def container_hover():
    return ft.Column(
        [
            ft.Text("Containers - hover"),
            ft.Row(
                [
                    ft.Container(width=100, height=100, bgcolor="red", ink=False, on_hover=lambda e: on_hover(e)),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Containers"
    page.add(
        ft.Column([
            container_clickable(),
            ft.Divider(),
            container_blur(page),
            ft.Divider(),
            container_hover(),
        ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )


ft.app(main)
