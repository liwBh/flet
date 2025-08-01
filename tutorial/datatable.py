import flet as ft


def make_columns(columns, text_color):
    cols = []
    for n, column in enumerate(columns):
        name = column.get("name")
        if not name:
            print(f"Skipping column {n}")
            continue

        col = ft.DataColumn(
            label=ft.Text(name, color=text_color),
            numeric=column.get("numeric", False),
        )
        tip = column.get("tooltip")

        if tip:
            col.tooltip = tip

        cols.append(col)

    return cols


def make_rows(columns, data, text_color):
    rows = []
    keys = [
        (col.get("key") or col["name"].lower().replace(" ", "_"))
        for col in columns
    ]

    for item in data:
        cells = [
            ft.DataCell(
                ft.Text(str(item.get(k, "")),
                        color=text_color),            )
            for k in keys
        ]
        rows.append(ft.DataRow(cells=cells))
    return rows


def create_datatable(
        columns,
        data,
        bgcolor=ft.Colors.WHITE,
        text_color=ft.Colors.BLACK,
        border_width=1,
        border_color=ft.Colors.BLACK,
        radius=5,
):
    return ft.DataTable(
        width=700,
        bgcolor=bgcolor,
        border=ft.border.all(border_width, border_color),
        border_radius=radius,
        sort_column_index=0,
        sort_ascending=True,
        vertical_lines=ft.border.BorderSide(border_width, border_color),
        horizontal_lines=ft.border.BorderSide(border_width, border_color),
        columns=make_columns(columns, text_color),
        rows=make_rows(columns, data, text_color),

    )


def main(page: ft.Page):
    columns = [
        {"name": "ID", "tooltip": "This is a first column", "numeric": False, "sort": True},
        {"name": "Name", "tooltip": "This is a second column", "numeric": False, "sort": True},
        {"name": "Last Name", "numeric": False, "sort": True},
        {"name": "Age", "numeric": True, "sort": False},
    ]
    data = [
        {"id": 1, "name": "Ana", "last_name": "Gómez", "age": 28},
        {"id": 2, "name": "Luis", "last_name": "Rojas", "age": 35},
        {"id": 3, "name": "Eva", "last_name": "Zamora", "age": 22},
    ]

    page.add(
        create_datatable(columns, data),
    )


ft.app(target=main)
