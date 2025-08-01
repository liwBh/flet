import flet as ft


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


def build_view_container() -> ft.Container:
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=10,
        content=ft.Column(
            controls=[
                container_clickable(),
                ft.Divider(),
            ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )
