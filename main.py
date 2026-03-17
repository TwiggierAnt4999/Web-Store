import flet as ft
from dataclasses import dataclass


# ===============================
# MODELO DE DATOS
# ===============================

@dataclass
class Producto:
    id: int
    nombre: str
    descripcion: str
    precio: float
    ruta_imagen: str


# ===============================
# COMPONENTE REUTILIZABLE
# ===============================

class TarjetaProducto(ft.Container):

    def __init__(self, producto: Producto):
        super().__init__()

        self.producto = producto

        self.width = 250
        self.padding = 15
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE
        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(2, 2)
        )

        self.content = ft.Column(
            [
                ft.Image(
                    src=producto.ruta_imagen,
                    width=200,
                    height=150,
                    fit="contain"
                ),

                ft.Text(
                    producto.nombre,
                    weight=ft.FontWeight.BOLD,
                    size=18
                ),

                ft.Text(
                    producto.descripcion,
                    size=12,
                    color=ft.Colors.GREY_700
                ),

                ft.Text(
                    f"${producto.precio}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN
                ),

                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                        ft.ElevatedButton("Agregar al carrito")
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=10
        )


# ===============================
# FUNCIÓN PRINCIPAL
# ===============================

def main(page: ft.Page):

    page.title = "TechStore"
    page.scroll = "auto"
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # ===============================
    # LISTA DE PRODUCTOS
    # ===============================

    productos = [

        Producto(1, "Laptop Gamer", "Laptop con RTX 4060 y 16GB RAM", 25999, "/laptop.png"),
        Producto(2, "Mouse Gamer", "Mouse RGB de alta precisión", 799, "/mouse.png"),
        Producto(3, "Teclado Mecánico", "Teclado RGB switches blue", 1299, "/teclado.png"),
        Producto(4, "Monitor 27 pulgadas", "Monitor 165Hz Full HD", 4999, "/monitor.png"),
        Producto(5, "Audífonos Gamer", "Audio envolvente 7.1", 1599, "/audifonos.png")

    ]


    # ===============================
    # CREAR TARJETAS
    # ===============================

    tarjetas = [TarjetaProducto(p) for p in productos]


    # ===============================
    # INTERFAZ
    # ===============================

    page.add(

        ft.Text("TechStore", size=40, weight=ft.FontWeight.BOLD),

        ft.Text(
            "Catálogo de productos tecnológicos",
            size=18,
            color=ft.Colors.GREY_700
        ),

        ft.Divider(),

        ft.Row(
            tarjetas,
            wrap=True,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


# 🔥 IMPORTANTE PARA WEB / RENDER
ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    assets_dir="assets"
)