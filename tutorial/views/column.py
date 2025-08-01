import flet as ft
import threading


def items(count):
    items = []
    for i in range(1, count + 1):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.Colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
        )
    return items


def spacing_slider_change(e):
    col.spacing = int(e.control.value)
    col.update()


gap_slider = ft.Slider(
    min=0,
    max=100,
    divisions=10,
    value=0,
    label="{value}",
    width=500,
    on_change=spacing_slider_change,
)

col = ft.Column(spacing=0, controls=items(5))

# --------------------------------------
HEIGHT = 400


def items2(count):
    items = []
    for i in range(1, count + 1):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=30,
                height=30,
                bgcolor=ft.Colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
        )
    return items


def slider_change(e):
    col2.height = float(e.control.value)
    col2.update()


width_slider = ft.Slider(
    min=0,
    max=HEIGHT,
    divisions=20,
    value=HEIGHT,
    label="{value}",
    width=500,
    on_change=slider_change,
)

col2 = ft.Column(
    wrap=True,
    spacing=10,
    run_spacing=10,
    controls=items(10),
    height=HEIGHT,
)
# --------------------------------------

def items3(count):
    items = []
    for i in range(1, count + 1):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.Colors.AMBER_500,
            )
        )
    return items


def column_with_alignment(align: ft.MainAxisAlignment):
    return ft.Column(
        [
            ft.Text(str(align), size=10),
            ft.Container(
                content=ft.Column(items(3), alignment=align),
                bgcolor=ft.Colors.AMBER_100,
                height=400,
            ),
        ]
    )

# --------------------------------------
def items4(count):
    items = []
    for i in range(1, count + 1):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.Colors.AMBER_500,
            )
        )
    return items


def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
    return ft.Column(
        [
            ft.Text(str(align), size=16),
            ft.Container(
                content=ft.Column(
                    items(5),
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=align,
                ),
                bgcolor=ft.Colors.AMBER_100,
                width=100,
            ),
        ]
    )

# --------------------------------------
cl = ft.Column(
    spacing=10,
    height=200,
    width=float("inf"),
    scroll=ft.ScrollMode.ALWAYS,
)
for i in range(0, 100):
    cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))


def scroll_to_offset(e):
    cl.scroll_to(offset=500, duration=1000)


def scroll_to_start(e):
    cl.scroll_to(offset=0, duration=1000)


def scroll_to_end(e):
    cl.scroll_to(offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)


def scroll_to_key(e):
    cl.scroll_to(key="20", duration=1000)


def scroll_to_delta(e):
    cl.scroll_to(delta=100, duration=200)


def scroll_to_minus_delta(e):
    cl.scroll_to(delta=-100, duration=200)


def build_view_column(page: ft.Page) -> ft.Container:
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=10,
        content=ft.Column(
            controls=[
                ft.Column([ft.Text("Spacing between items"), gap_slider]),
                col,
                ft.Divider(),
                ft.Column(
                    [
                        ft.Text(
                            "Change the column height to see how child items wrap onto multiple columns:"
                        ),
                        width_slider,
                    ]
                ),
                ft.Container(content=col2, bgcolor=ft.Colors.TRANSPARENT),
                ft.Divider(),
                ft.Row(
                    [
                        column_with_alignment(ft.MainAxisAlignment.START),
                        column_with_alignment(ft.MainAxisAlignment.CENTER),
                        column_with_alignment(ft.MainAxisAlignment.END),
                        column_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),
                        column_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),
                        column_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),
                    ],
                    spacing=30,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(),
                ft.Row(
                    [
                        column_with_horiz_alignment(ft.CrossAxisAlignment.START),
                        column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER),
                        column_with_horiz_alignment(ft.CrossAxisAlignment.END),
                        column_with_horiz_alignment(ft.CrossAxisAlignment.BASELINE),
                        column_with_horiz_alignment(ft.CrossAxisAlignment.STRETCH),
                    ],
                    spacing=30,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(),
                ft.Text("Infinite scroll", size=16),
                ft.Container(cl, border=ft.border.all(1)),
                ft.ElevatedButton("Scroll to offset 500", on_click=scroll_to_offset),
                ft.Row(
                    [
                        ft.ElevatedButton("Scroll -100", on_click=scroll_to_minus_delta),
                        ft.ElevatedButton("Scroll +100", on_click=scroll_to_delta),
                    ]
                ),
                ft.ElevatedButton("Scroll to key '20'", on_click=scroll_to_key),
                ft.Row(
                    [
                        ft.ElevatedButton("Scroll to start", on_click=scroll_to_start),
                        ft.ElevatedButton("Scroll to end", on_click=scroll_to_end),
                    ]
                ),
            ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )
