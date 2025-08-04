
import flet as ft

def build_view_home(page: ft.Page) -> ft.Container:
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=10,
        content=ft.Column(
            controls=[
                ft.Text("Casita", color=ft.Colors.BLACK, size=20),
            ],
            alignment=ft.alignment.center,
        )
    )