
import flet as ft
from config.nav_bar import NavBar
from routes.routes import router


class ProductPage(ft.View):
    def __init__(self, page, img_src, title, sub_title, price, rating):
        super().__init__(bgcolor="#0c0f14")
        self.page = page
        self.img_src = img_src
        self.title = title
        self.sub_title = sub_title
        self.price = price
        self.rating = rating

        self.color_coffe = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        self.nav_Color = "#18191b"
        self.build_view()

    def build_view(self):
        self.controls.append(
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor=self.bg_color,
                margin=10,
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        ft.Stack(
                            expand=8,
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    border_radius=20,
                                    content=ft.Image(src=f"assets/coffees/{self.img_src}.png",
                                                     fit=ft.ImageFit.COVER, width=350, height=400)
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Container(
                                            margin=10,
                                            on_click=self.close_product_page,
                                            width=30, height=30, border_radius=10, bgcolor=ft.Colors.BLACK,
                                            content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT, color=self.color_coffe)
                                        ),
                                        ft.Container(
                                            margin=10,
                                            on_click=self.add_favorite,
                                            width=30, height=30, border_radius=10, bgcolor=ft.Colors.BLACK,
                                            content=ft.Icon(ft.Icons.FAVORITE, color=self.color_coffe)
                                        )
                                    ]
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors.with_opacity(0.6, ft.Colors.BLACK),
                                    expand=True,
                                    padding=20,
                                    alignment=ft.alignment.center_left,
                                    margin=ft.margin.only(top=200),
                                    shadow=[
                                        ft.BoxShadow(
                                            spread_radius=15, blur_radius=20,
                                            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                        )
                                    ],
                                    content=ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(self.title, size=30, weight=ft.FontWeight.BOLD),
                                            ft.Text(self.sub_title, size=20, weight=ft.FontWeight.BOLD),
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(ft.Icons.STAR, color=self.color_coffe),
                                                    ft.Text(self.price, weight=ft.FontWeight.BOLD),
                                                ],
                                                spacing=5
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        ft.Container(
                            height=30,
                            alignment=ft.alignment.center_left,
                            content=ft.Text("Tamaño"),
                        ),
                        ft.Row(
                            expand=1,
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.ElevatedButton("S", color=ft.Colors.WHITE, bgcolor=self.container_color,
                                                  width=80, style=ft.ButtonStyle(
                                        overlay_color=self.color_coffe,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(1, self.color_coffe)
                                    )),
                                ft.ElevatedButton("M", color=ft.Colors.WHITE, bgcolor=self.container_color,
                                                  width=80, style=ft.ButtonStyle(
                                        overlay_color=self.color_coffe,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(1, self.color_coffe)
                                    )),
                                ft.ElevatedButton("L", color=ft.Colors.WHITE, bgcolor=self.container_color,
                                                  width=80, style=ft.ButtonStyle(
                                        overlay_color=self.color_coffe,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(1, self.color_coffe)
                                    )),
                            ]
                        ),
                        ft.Container(
                            height=30,
                            alignment=ft.alignment.center_left,
                            content=ft.Text("Precio"),
                        ),
                        ft.Row(
                            expand=1,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    size=20,
                                    spans=[
                                        ft.TextSpan("$", style=ft.TextStyle(color=self.color_coffe,
                                                                            weight=ft.FontWeight.BOLD)),
                                        ft.TextSpan(f"{self.price}", style=ft.TextStyle(color=ft.Colors.WHITE,
                                                                                        weight=ft.FontWeight.BOLD))
                                    ]
                                ),
                                ft.ElevatedButton("Comprar", color=ft.Colors.WHITE, bgcolor=self.container_color,
                                                  width=180, style=ft.ButtonStyle(
                                        overlay_color=self.color_coffe,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(1, self.color_coffe)
                                    )),
                            ]
                        )
                    ]
                )
            )
        )
        pass

    def close_product_page(self, e):
        self.page.views.pop()
        self.page.update()
        pass

    def add_favorite(self, e):
        print(1)


class ProductCard(ft.Container):
    def __init__(self, page, img_src, title, sub_title, price, rating, category):
        super().__init__(
            alignment=ft.alignment.center,
            width=150,
            height=150,
            border_radius=10,
            bgcolor="#141821",
            padding=10,
            margin=ft.margin.only(top=10),
            expand=False,
        )
        self.page = page
        self.img_src = img_src
        self.title = title
        self.sub_title = sub_title
        self.price = price
        self.rating = rating
        self.category = category
        self.color_coffe = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        self.content = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            border_radius=10,
                            on_click=self.show_container,
                            content=ft.Image(src=f"assets/coffees/{self.img_src}.png",
                                             width=150, fit=ft.ImageFit.COVER, height=100),
                        ),
                        ft.Container(
                            width=60,
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.only(top_left=10, bottom_right=10),
                            bgcolor=ft.Colors.with_opacity(0.6, ft.Colors.BLACK),
                            content=ft.Row(
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.STAR, color=self.color_coffe),
                                    ft.Text(f"{self.rating}", weight=ft.FontWeight.BOLD),
                                ]
                            ),
                        )
                    ]
                ),
                ft.Text(value=self.title, weight=ft.FontWeight.BOLD),
                ft.Text(value=self.sub_title, weight=ft.FontWeight.BOLD, color="#5a5a5a"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan("$", style=ft.TextStyle(color=self.color_coffe, size=15,
                                                                    weight=ft.FontWeight.BOLD)),
                                ft.TextSpan(f"{self.price}", style=ft.TextStyle(color=ft.Colors.WHITE, size=15,
                                                                                weight=ft.FontWeight.BOLD))
                            ]
                        ),
                        ft.Container(
                            content=ft.Icon(ft.Icons.ADD, color=ft.Colors.WHITE),
                            bgcolor=self.color_coffe, width=30, height=30, border_radius=10,
                            on_click=self.add_favorites
                        )
                    ]
                )
            ]
        )

    def show_container(self, e):
        product_view = ProductPage(self.page, self.img_src, self.title, self.sub_title, self.price, self.rating)
        self.page.views.append(product_view)
        self.page.update()
        pass

    def add_favorites(self, e):
        pass


class AppShopCoffee(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.color_coffe = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        self.nav_color = "#18191b"
        self.page.spacing = 5
        self.page.padding = 5
        self.page.bgcolor = self.bg_color
        self.page.fonts = {"Poppins": "Poppins-Regular.ttf"}
        self.page.theme = ft.Theme(
            scrollbar_theme=ft.ScrollbarTheme(
                thumb_color=self.color_coffe
            ),
            font_family="Poppins",
        )
        self.nav = NavBar(self.page).nav_buttons
        self.page.navigation_bar = self.nav

        self.products = [
            ProductCard(self.page, "cappuccino1", "Capuchino", "Siente el aroma, ama el sabor", "12.50", "4.9", "cappuccino"),
            ProductCard(self.page, "cappuccino2", "Capuchino", "Siente el aroma, ama el sabor", "12.50", "4.9", "cappuccino"),
            ProductCard(self.page, "cappuccino3", "Capuchino", "Siente el aroma, ama el sabor", "12.50", "4.9", "cappuccino"),
            ProductCard(self.page, "macchiato1", "Machiato", "Siente el aroma, ama el sabor", "12.50", "4.9", "macchiato"),
            ProductCard(self.page, "macchiato2", "Machiato", "Siente el aroma, ama el sabor", "12.50", "4.9", "macchiato"),
            ProductCard(self.page, "macchiato3", "Machiato", "Siente el aroma, ama el sabor", "12.50", "4.9", "macchiato"),
            ProductCard(self.page, "latte1", "Latte", "Siente el aroma, ama el sabor", "12.50", "4.9", "latte"),
            ProductCard(self.page, "latte2", "Latte", "Siente el aroma, ama el sabor", "12.50", "4.9", "latte"),
            ProductCard(self.page, "latte3", "Latte", "Siente el aroma, ama el sabor", "12.50", "4.9", "latte"),
        ]

        self.grid_view = ft.GridView(
            runs_count=2,
            child_aspect_ratio=0.6,
            controls=self.products
        )

        def filtro_de_productos(category):
            filtered_products = []
            for product in self.products:
                if product.category == category:
                    filtered_products.append(product)
            return filtered_products

        self.home_view = ft.Container(
            padding=10,
            offset=(0, 0),
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE
                            ),
                            ft.Container(
                                ft.Image(src="assets/avatar.jpg", height=30, ),
                                border_radius=10
                            )
                        ]
                    ),
                    ft.Text("Encuentre el mejor \n café para ti", size=25, weight=ft.FontWeight.BOLD),
                    ft.TextField(prefix_icon=ft.Icons.SEARCH, hint_text="Encuentra tu café", border_radius=10,
                                 bgcolor=self.container_color, border_color=ft.Colors.TRANSPARENT,
                                 on_change=self.filter_products),
                    ft.Container(expand=True,
                                 content=ft.Tabs(
                                     selected_index=0,
                                     expand=True,
                                     indicator_color=ft.Colors.TRANSPARENT,
                                     label_color=self.color_coffe,
                                     tabs=[
                                         ft.Tab(text="Todos",
                                                content=self.grid_view
                                                ),
                                         ft.Tab(text="Americano",
                                                content=ft.GridView(
                                                    runs_count=2,
                                                    child_aspect_ratio=0.6,
                                                    controls=filtro_de_productos("americano")

                                                )),
                                         ft.Tab(text="Capuchino",
                                                content=ft.GridView(
                                                    runs_count=2,
                                                    child_aspect_ratio=0.6,
                                                    controls=filtro_de_productos("cappuccino")
                                                )),
                                         ft.Tab(text="Micchiato",
                                                content=ft.GridView(
                                                    runs_count=2,
                                                    child_aspect_ratio=0.6,
                                                    controls=filtro_de_productos("macchiato")
                                                )),
                                     ]
                                 )
                                 )
                ]
            )
        )

        self.store_view = ft.Container(
            expand=True,
            offset=(0, 0),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Tienda", size=20, ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src="assets/coffees/americano1.jpg",
                            fit=ft.ImageFit.CONTAIN, width=100,
                        )
                    )
                ]
            )
        )

        self.favorites_view = ft.Container(
            expand=True,
            offset=(0, 0),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Favoritos", size=20, ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src="assets/coffees/americano3.jpg",
                            fit=ft.ImageFit.CONTAIN, width=120,
                        )
                    )
                ]
            )
        )

        self.notifications_view = ft.Container(
            expand=True,
            offset=(0, 0),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Notificaciones", size=20, ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src="assets/coffees/americano2.jpg",
                            fit=ft.ImageFit.CONTAIN, width=120,
                        )
                    )
                ]
            )
        )
        self.views = [
            {"route": "/home", "view": self.home_view},
            {"route": "/store", "view": self.store_view},
            {"route": "/favorites", "view": self.favorites_view},
            {"route": "/notifications", "view": self.notifications_view}
        ]


        self.page.on_route_change = lambda r: router(self, self.page.route, self.views)
        self.page.go("/home")

    def filter_products(self, e):
        search_text = e.control.value
        filtered_products = [
            product for product in self.products if search_text.lower() in product.title.lower()
        ]
        self.grid_view.controls = filtered_products
        self.grid_view.update()




ft.app(target=AppShopCoffee)
