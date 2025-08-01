import flet as ft
from components.color_picker import color_picker

def change_theme_mode(e, page, sw):
    if page.theme_mode == ft.ThemeMode.DARK:
        page.theme_mode = ft.ThemeMode.LIGHT
        sw.thumb_icon = ft.Icons.LIGHT_MODE
    else:
        sw.thumb_icon = ft.Icons.DARK_MODE
        page.theme_mode = ft.ThemeMode.DARK
    page.update()

def on_color_change(color, page, preview):
    page.theme = ft.Theme(color_scheme_seed=color)
    preview.bgcolor = color
    page.update()

def main(page: ft.Page):
    page.title = "Theme"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.WHITE,
    )

    preview = ft.Container(width=36, height=36,
                           bgcolor=page.theme.color_scheme_seed,
                           border_radius=8,
                           border=ft.border.all(1, ft.Colors.GREY_400),
                           )

    sw = ft.Switch(thumb_icon=ft.Icons.DARK_MODE, on_change=lambda e: change_theme_mode(e, page, sw))

    picker_icon = color_picker(page, callback=lambda color: on_color_change(color, page, preview))

    settings = ft.Row(
        [preview, picker_icon, sw],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )

    page.add(
        # Page theme
        ft.Row(
            [
                ft.Container(
                    content=ft.ElevatedButton("Page theme button"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                    padding=20,
                    width=300,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Settings", size=12),
                            settings
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(bottom=50),
                    alignment=ft.alignment.top_right,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        # Inherited theme with primary color overridden
        ft.Container(
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
            content=ft.ElevatedButton("Inherited theme button"),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            padding=20,
            width=300,
        ),
        # Unique always DARK theme
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Unique theme button"),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            padding=20,
            width=300,
        ),
    )


ft.app(main)