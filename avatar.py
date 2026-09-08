import json
import os

ARCHIVO_USUARIOS = "usuarios.json"


def cargar_usuarios():

    if not os.path.exists(ARCHIVO_USUARIOS):
        return []

    try:
        with open(
            ARCHIVO_USUARIOS,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    except:
        return []


def guardar_usuarios(usuarios):

    with open(
        ARCHIVO_USUARIOS,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            usuarios,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def buscar_usuario(apodo):

    usuarios = cargar_usuarios()

    for usuario in usuarios:

        if usuario["apodo"].lower() == apodo.lower():
            return usuario

    return None


def registrar_usuario():

    usuarios = cargar_usuarios()

    print("\n===== REGISTRO DE USUARIO =====")

    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()

    while True:

        apodo = input("Apodo: ").strip()

        if buscar_usuario(apodo):

            print("\nEse apodo ya existe.")
            print("Debe elegir otro.")

        else:
            break

    celular = input("Celular: ").strip()

    descripcion = input(
        "Descripción del avatar: "
    ).strip()

    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "apodo": apodo,
        "celular": celular,
        "descripcion": descripcion
    }

    usuarios.append(usuario)

    guardar_usuarios(usuarios)

    print("\nUsuario registrado exitosamente.")

    return usuario


def eliminar_historial_usuario(apodo):

    archivo_historial = "historial.json"

    if not os.path.exists(archivo_historial):
        return

    try:

        with open(
            archivo_historial,
            "r",
            encoding="utf-8"
        ) as archivo:

            historial = json.load(archivo)

    except:

        historial = []

    historial_filtrado = []

    for partida in historial:

        if partida["apodo"].lower() != apodo.lower():

            historial_filtrado.append(partida)

    with open(
        archivo_historial,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            historial_filtrado,
            archivo,
            indent=4,
            ensure_ascii=False
        )

def eliminar_progreso_usuario(apodo):

    archivo_progreso = "progreso.json"

    if not os.path.exists(archivo_progreso):
        return

    try:

        with open(
            archivo_progreso,
            "r",
            encoding="utf-8"
        ) as archivo:

            progreso = json.load(archivo)

    except:

        return

    if progreso.get("apodo", "").lower() == apodo.lower():

        os.remove(archivo_progreso)


def iniciar_sesion():

    print("\n===== INICIAR SESIÓN =====")

    apodo = input(
        "Ingrese su apodo: "
    ).strip()

    usuario = buscar_usuario(apodo)

    if usuario:

        print(
            f"\nBienvenido {usuario['apodo']}"
        )

        return usuario

    print("\nUsuario no encontrado.")

    return None


def eliminar_usuario():

    usuarios = cargar_usuarios()

    print("\n===== ELIMINAR USUARIO =====")

    apodo = input(
        "Ingrese el apodo a eliminar: "
    ).strip()

    usuario_encontrado = None

    for usuario in usuarios:

        if usuario["apodo"].lower() == apodo.lower():

            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:

        print("\nUsuario no encontrado.")
        return

    confirmar = input(
        f"¿Está seguro de eliminar a {apodo}? (S/N): "
    ).upper()

    if confirmar != "S":

        print("\nOperación cancelada.")
        return

    # Eliminar usuario
    usuarios.remove(usuario_encontrado)

    guardar_usuarios(usuarios)

    # Eliminar historial
    eliminar_historial_usuario(apodo)

# Eliminar progreso guardado
    eliminar_progreso_usuario(apodo)

    print(
    "\nUsuario, historial y progreso eliminados correctamente."
    )

def mostrar_usuarios():

    usuarios = cargar_usuarios()

    if len(usuarios) == 0:

        print("\nNo hay usuarios registrados.")
        return

    print("\n===== USUARIOS REGISTRADOS =====")

    for usuario in usuarios:

        print(
            f"Apodo: {usuario['apodo']}"
        )