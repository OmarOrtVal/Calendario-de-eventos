import flet as ft

def main(page:ft.Page):
    page.title = "Imagen"
    page.add(ft.Text("Hello, World!"))
    page.add(ft.TextField(
    label="Nombre",
    hint_text="Ingresa tu nombre",
    value="",
    prefix_icon=ft.Icons.PERSON,
    suffix_text=".com",
    helper_text="Máximo 50 caracteres",
    error_text="Campo obligatorio",
    password=False,
    can_reveal_password=False,
    multiline=False,
    max_length=50,
    keyboard_type=ft.KeyboardType.TEXT,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.Colors.BLUE,
    focused_border_color=ft.Colors.RED,
    filled=True,
    bgcolor=ft.Colors.GREY_100,
    on_change=lambda e: print(e.control.value),
    on_submit=lambda e: print("Enter presionado")
    )
)
ft.run(main)