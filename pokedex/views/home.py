import flet as ft
from config.configPage import app_color, app_size, AppState
import flet.canvas as cv
import controller.home_controller as controller

def section_header():
    led = ft.Container(width=40, height=40, left=4, top=4, bgcolor=app_color["blue"], border_radius=50)

    btn_blue = ft.Stack(
        controls=[
            ft.Container(width=50, height=50, bgcolor=app_color["white"], border_radius=50),
            led,
        ]
    )
    items = [
        ft.Container(content=btn_blue, width=50, height=50, border=ft.border.all(color=app_color["black"], width=1),
                     border_radius=50),
        ft.Container(width=20, height=20, border=ft.border.all(color=app_color["black"], width=1),
                     bgcolor=app_color["red"], border_radius=50),
        ft.Container(width=20, height=20, border=ft.border.all(color=app_color["black"], width=1),
                     bgcolor=app_color["yellow"], border_radius=50),
        ft.Container(width=20, height=20, border=ft.border.all(color=app_color["black"], width=1),
                     bgcolor=app_color["green"], border_radius=50),
    ]
    header = ft.Container(
        width=400,
        height=60,
        content=ft.Row(controls=items, expand=False),
        margin=ft.margin.only(top=20),
        # border=ft.border.all(color=app_color["black"], width=2),
        alignment=ft.alignment.center,
        expand=False,
    )

    return header, led


def create_triangle():
    return cv.Canvas([
        cv.Path(
            [
                cv.Path.MoveTo(20, 5),
                cv.Path.LineTo(0, 35),
                cv.Path.LineTo(40, 35),
            ],
            paint=ft.Paint(
                style=ft.PaintingStyle.FILL,
                color=app_color["black"],  # usa color explícito
            )
        ),
    ],
        width=40,
        height=40,
    )


def create_btns(text, page, image, led):
    async def on_add(e):
        await controller.event_change(e, action="add", page=page, text=text, image=image, led=led)

    async def on_subtract(e):
        await controller.event_change(e, action="subtract", page=page, text=text, image=image, led=led)

    return ft.Column(
        [
            ft.Container(content=create_triangle(),
                         on_click=on_add,
                         width=40, height=40,
                         alignment=ft.alignment.center),  # arrow top
            # radianes 180 grados = 3.14159
            ft.Container(content=create_triangle(),
                         on_click=on_subtract,
                         width=40, height=40,
                         rotate=ft.Rotate(angle=3.14159),
                         alignment=ft.alignment.center),  # arrow bottom
        ],
        spacing=0,
        expand=False,
        alignment=ft.alignment.center
    )


def section_footer(page, image, led):
    text = ft.Text("...", size=14, color=app_color["black"])
    items = [
        ft.Container(width=18),  # margen izq.
        ft.Container(text, width=290,height=238, bgcolor=app_color["green"],
                     padding=ft.padding.all(10),
                     alignment=ft.alignment.center,
                     border_radius=10),  # info
        ft.Container(content=create_btns(text, page, image, led),
                     width=45, height=90, alignment=ft.alignment.center,
                     ),  # btns
        ft.Container(width=18),  # margen der.
    ]
    footer = ft.Container(
        width=400,
        height=240,
        content=ft.Row(controls=items, expand=False), margin=ft.margin.only(top=40),
        expand=False,
    )

    return footer


def section_main():
    center_x = (399 - 50) / 2
    center_y = (259 - 50) / 2
    image = ft.Image(
        src=AppState.get_image(),
        scale=5,
        width=50,
        height=50,
        top=center_y,
        left=center_x,
    )

    central = ft.Stack(
        controls=[
            ft.Container(width=399, height=259, bgcolor=app_color["white"], border_radius=5),
            ft.Container(width=370, height=230, top=15, left=15, bgcolor=app_color["black"], border_radius=5),
            image
        ],
        expand=False,
    )
    main = ft.Container(
        content=central,
        width=400,
        height=260,
        margin=ft.margin.only(top=20),
        border=ft.border.all(color=app_color["black"], width=1),
        alignment=ft.alignment.center,
        border_radius=5,
        expand=False,
    )

    return main, image


async def page_home(page):
    main, image = section_main()
    header, led = section_header()

    layout = ft.Column(
        controls=[
            header,
            main,
            section_footer(page, image, led),
        ],
        expand=True,
    )

    container = ft.Container(
        width=app_size["width"],
        height=app_size["height"],
        bgcolor=app_color["primary"],
        content=layout,
        alignment=ft.alignment.top_center,
        expand=True,
    )

    page.add(container)
    page.update()
    await controller.blink(page, led)
