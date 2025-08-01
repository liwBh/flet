import flet as ft

def create_card():
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    # header
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.ALBUM),
                        title=ft.Text("My title"),
                        subtitle=ft.Text("My subtitle"),
                    ),
                    ft.Divider(),
                    # body
                    ft.Container(
                        content=ft.Column(
                        [
                            ft.Text("Description: my description"),
                            ft.Text("Price: my price"),
                        ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=10,
                        expand=True,
                    ),
                    ft.Divider(),
                    # footer
                    ft.Row(
                        [ft.TextButton("Accept"), ft.TextButton("Cancel")],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                ]
            ),
            width=400,
            padding=10,
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(1, ft.Colors.GREY_400),
        ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
    )


def build_view_card() -> ft.Container:
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=10,
        content=ft.Column(
            controls=[
                create_card(),
            ]
        )
    )

