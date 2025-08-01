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


def main(page: ft.Page):
    page.title = "Card Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        create_card(),
    )


ft.app(main)
