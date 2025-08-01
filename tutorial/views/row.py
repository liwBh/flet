import flet as ft


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


def spacing_slider_change(e, row, text):
    row.spacing = int(e.control.value)
    text.value = f"spacing={str(row.spacing)}"
    row.update()
    text.update()


def width_slider_change(e, row, text, slider):
    if not row.wrap:
        slider.value = row.width
        slider.update()
        return

    row.width = float(e.control.value)
    text.value = f"width={str(row.width)}, wrap={str(row.wrap)}"
    row.update()
    text.update()


def toggle_wrap(e, row, text):
    row.wrap = bool(e.control.value)
    text.value = f"width={str(row.width)}, wrap={str(row.wrap)}"
    row.update()
    text.update()


def alignment_slider_change(e, row, text, type="horizontal"):
    v = int(e.control.value)
    mapping_v = {
        1: ft.CrossAxisAlignment.START,
        2: ft.CrossAxisAlignment.CENTER,
        3: ft.CrossAxisAlignment.END,
    }
    mapping_h = {
        1: ft.MainAxisAlignment.START,
        2: ft.MainAxisAlignment.CENTER,
        3: ft.MainAxisAlignment.END,
        4: ft.MainAxisAlignment.SPACE_BETWEEN,
        5: ft.MainAxisAlignment.SPACE_AROUND,
        6: ft.MainAxisAlignment.SPACE_EVENLY,
    }

    if type == "horizontal":
        alignment = mapping_h.get(v, ft.MainAxisAlignment.START)
        row.alignment = alignment
        text.value = f"alignment={str(alignment)}"
    else:
        alignment = mapping_v.get(v, ft.CrossAxisAlignment.START)
        row.vertical_alignment = alignment
        text.value = f"vertical_alignment={str(alignment)}"

    row.update()
    text.update()


def row_spacing():
    row = ft.Row(spacing=0, controls=items(10), scroll=ft.ScrollMode.AUTO)
    text = ft.Text(f"spacing={str(row.spacing)}", size=12)

    gap_slider = ft.Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label="{value}",
        on_change=lambda e: spacing_slider_change(e, row, text),
    )

    return ft.Column([
        ft.Text("Row spacing", size=16),
        gap_slider,
        text,
        row]
    )


def row_wrap(page):
    row = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(30),
        width=page.window.width,
    )
    text = ft.Text(f"wrap={str(row.wrap)}", size=12)
    width_slider = ft.Slider(
        min=0,
        max=page.window.width,
        divisions=20,
        value=page.window.width,
        label="{value}",
        on_change=lambda e: width_slider_change(e, row, text, width_slider),
    )
    has_wrap = ft.Checkbox(
        label="wrap",
        value=row.wrap,
        on_change=lambda e: toggle_wrap(e, row, text),
    )

    return ft.Column(
        [
            ft.Text("Row wrapping", size=16),
            width_slider,
            has_wrap,
            text,
            row,
        ],
    )


def row_alignment_horizontal():
    row = ft.Row(controls=items(3), alignment=ft.MainAxisAlignment.START, height=100)
    text = ft.Text(f"alignment={str(ft.MainAxisAlignment.START)}", size=12)

    alignment_slider = ft.Slider(
        min=1,
        max=6,
        divisions=5,
        value=1,
        label="{value}",
        on_change=lambda e: alignment_slider_change(e, row, text),
    )

    return ft.Column([
        ft.Text("Row horizontal alignments", size=16),
        alignment_slider,
        text,
        ft.Container(
            content=row,
            bgcolor=ft.Colors.BLUE,
        ),
    ])


def row_alignment_vertical():
    row = ft.Row(controls=items(3), vertical_alignment=ft.CrossAxisAlignment.START)
    text = ft.Text(f"vertical_alignment={str(ft.CrossAxisAlignment.START)}", size=12)

    alignment_slider = ft.Slider(
        min=1,
        max=3,
        divisions=2,
        value=1,
        label="{value}",
        on_change=lambda e: alignment_slider_change(e, row, text, "vertical"),
    )

    return ft.Column([
        ft.Text("Row vertical alignments", size=16),
        alignment_slider,
        text,
        ft.Container(
            content=row,
            bgcolor=ft.Colors.BLUE,
            height=150,
        ),
    ])


def build_view_row(page: ft.Page) -> ft.Container:
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=10,
        content=ft.Column(
            controls=[
                row_spacing(),
                ft.Divider(),
                row_wrap(page),
                ft.Divider(),
                row_alignment_horizontal(),
                row_alignment_vertical(),
            ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )
