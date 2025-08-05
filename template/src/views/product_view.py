import flet as ft
import os
import shutil

from controls.product_control import ProductControl

class ProductView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.product_control = ProductControl()
        self.products = []
        self.name_field = ft.TextField(label="Nombre del producto")
        self.code_field = ft.TextField(label="Código del producto")
        self.price_field = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER)
        self.selected_image_path = ""
        self.image_display = ft.Text("Ninguna imagen seleccionada")

        self.file_picker = ft.FilePicker(on_result=self.on_image_selected)
        self.page.overlay.append(self.file_picker)

        self.image_picker_controls = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Seleccionar Imagen",
                    icon=ft.Icons.IMAGE,
                    on_click=lambda _: self.file_picker.pick_files(
                        allow_multiple=False,
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ),
                self.image_display
            ],
            spacing=10
        )

        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Agregar nuevo producto"),
            content=ft.Column(
                controls=[
                    self.name_field,
                    self.code_field,
                    self.image_picker_controls,
                    self.price_field,
                ],
                tight=True,
                spacing=10
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: self.close_dialog()),
                ft.ElevatedButton("Guardar", on_click=self.submit_product),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.overlay.append(self.dialog)

    def on_add_product(self, e):
        self.clear_form()
        self.dialog.title = ft.Text("Agregar nuevo producto")
        self.dialog.open = True
        self.page.update()

    def close_dialog(self):
        self.dialog.open = False
        self.page.update()

    def clear_form(self):
        self.name_field.value = ""
        self.code_field.value = ""
        self.price_field.value = ""
        self.selected_image_path = ""
        self.image_display.value = "Ninguna imagen seleccionada"
        self.page.update()

    def on_image_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.selected_image_path = e.files[0].path
            file_name = os.path.basename(self.selected_image_path)
            self.image_display.value = f"Seleccionada: {file_name}"
        else:
            self.selected_image_path = ""
            self.image_display.value = "Ninguna imagen seleccionada"
        self.page.update()

    def get_selected_image_name(self):
        return os.path.basename(self.selected_image_path) if self.selected_image_path else ""

    def submit_product(self, e):
        for control in [self.name_field, self.code_field, self.price_field]:
            control.error_text = ""

        name = self.name_field.value.strip()
        code = self.code_field.value.strip()
        image_name = self.get_selected_image_name()
        price = self.price_field.value.strip()

        if not name:
            self.name_field.error_text = "Este campo es obligatorio"
            self.page.update()
            return
        if not code:
            self.code_field.error_text = "Este campo es obligatorio"
            self.page.update()
            return
        if not price:
            self.price_field.error_text = "Este campo es obligatorio"
            self.page.update()
            return
        if not image_name:
            self.image_display.value = "Ninguna imagen seleccionada"
            self.page.update()
            return

        try:
            price_value = float(price)
            if price_value < 0:
                raise ValueError
        except ValueError:
            self.price_field.error_text = ft.Text("El precio debe ser un número positivo", color=ft.Colors.RED)
            self.page.update()
            return
        try:
            self.products.append(self.product_control.create_product(name, code, price_value, image_name))
            self.dialog.open = False
            self.product_list_container.controls = self.build_product_cards()
            self.product_list_container.update()
            self.page.update()
        except Exception as ex:
            print(f"Error al agregar producto: {ex}")
            self.dialog.title = ft.Text(ex, color=ft.Colors.RED)
            self.page.update()
        try:
            os.makedirs("src/assets/image", exist_ok=True)
            shutil.copy(self.selected_image_path, os.path.join("src/assets/image", image_name))
        except Exception as ex:
            print(f"Error al copiar imagen: {ex}")
        self.page.update()

    def build_product_cards(self):
        self.products = self.product_control.get_all_products()
        return [
            ft.Container(
                content=ft.Card(
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(
                                    src=f"/image/{product.image}",
                                    fit=ft.ImageFit.COVER,
                                    width=300,
                                    height=200,
                                ),
                                ft.Divider(color=ft.Colors.GREY_300),
                                ft.Text(product.name, size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"${product.price:.2f}", size=14),
                                ft.Text(product.code, size=12, color=ft.Colors.GREY_600),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        padding=10,
                        width=300,
                    )
                ),
                width=320,
                height=360,
                padding=5,
            )
            for product in self.products
        ]

    def build_view_product(self) -> ft.Container:

        self.product_list_container = ft.Column(
            controls=self.build_product_cards(),
            scroll=ft.ScrollMode.AUTO,
            spacing=15,
            wrap=False,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLUE_GREY_50,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        padding=ft.Padding(20, 10, 20, 10),
                        content=ft.Row(
                            controls=[
                                ft.Text("Productos", size=22, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                                ft.ElevatedButton(
                                    text="Agregar",
                                    icon=ft.Icons.ADD,
                                    bgcolor=ft.Colors.AMBER,
                                    color=ft.Colors.BLACK,
                                    on_click=self.on_add_product,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ),
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=self.product_list_container,
                        alignment=ft.alignment.center,
                    )
                ]
            )
        )
