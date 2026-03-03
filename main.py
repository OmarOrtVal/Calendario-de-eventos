import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Mi Formulario de Eventos"
    page.padding = 20
    page.scroll = "adaptive"
    
    def handle_change(e: ft.Event[ft.DatePicker]):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%m/%d/%Y')}"))

    def handle_dismissal(e: ft.Event[ft.DialogControl]):
        page.add(ft.Text("DatePicker dismissed"))

    today = datetime.datetime.now()

    d = ft.DatePicker(
        first_date=datetime.datetime(year=today.year - 1, month=1, day=1),
        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    titulo = ft.Text(
        "REGISTRO DE EVENTOS",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
    )

    nombre = ft.TextField(
        label="Nombre del evento",
        width=400,
    )

    tipo = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia",
        width=400,
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial",
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False,
    )
    
    page.add(
        ft.Button(
            content="Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.show_dialog(d),
        )
    )
    
    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        value=4,
        label="{value} horas",
        width=400,
    )

    txt_duracion = ft.Text("Duración seleccionada: 4 horas")

    def cambiar_duracion(e):
        txt_duracion.value = f"Duración seleccionada: {int(duracion.value)} horas"
        page.update()

    duracion.on_change = cambiar_duracion

    resumen = ft.Text(
        value="",
        size=16,
    )

    linea = ft.Divider(height=20)

    def mostrar_resumen(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR: El nombre del evento no puede estar vacío"
            resumen.color = ft.Colors.RED
        else:
            resumen.value = f"""
            RESUMEN DEL EVENTO
            Nombre: {nombre.value}
            Tipo: {tipo.value}
            Modalidad: {modalidad.value}
            Inscripción: {'Sí' if inscripcion.value else 'No'}
            Duración: {int(duracion.value)} horas
            """
            resumen.color = ft.Colors.BLACK

        page.update()

    boton = ft.ElevatedButton(
        "MOSTRAR RESUMEN",
        on_click=mostrar_resumen,
        width=200,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    ft.ListView(
    controls=[ft.Text(f"Item {i}") for i in range(1, 6)],
    )

    page.add(
        titulo,
        ft.Container(height=10),
        nombre,
        ft.Container(height=10),
        tipo,
        ft.Container(height=10),
        ft.Text("Modalidad:"),
        modalidad,
        ft.Container(height=10),
        inscripcion,
        ft.Container(height=10),
        ft.Text("Duración:"),
        duracion,
        txt_duracion,
        ft.Container(height=20),
        boton,
        linea,
        resumen,
    )

ft.run(main)