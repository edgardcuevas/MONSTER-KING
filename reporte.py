import json
import os


ARCHIVO_PROGRESO = "progreso.json"
ARCHIVO_HISTORIAL = "historial.json"


def guardar_progreso(datos):

    with open(
        ARCHIVO_PROGRESO,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def cargar_progreso():

    if not os.path.exists(ARCHIVO_PROGRESO):
        return None

    try:

        with open(
            ARCHIVO_PROGRESO,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    except:
        return None


def eliminar_progreso():

    if os.path.exists(ARCHIVO_PROGRESO):

        os.remove(ARCHIVO_PROGRESO)


def cargar_historial():

    if not os.path.exists(ARCHIVO_HISTORIAL):
        return []

    try:

        with open(
            ARCHIVO_HISTORIAL,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    except:
        return []


def guardar_historial_partida(partida):

    historial = cargar_historial()

    historial.append(partida)

    with open(
        ARCHIVO_HISTORIAL,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            historial,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def mostrar_historial(apodo):

    historial = cargar_historial()

    partidas_usuario = []

    for partida in historial:

        if partida["apodo"].lower() == apodo.lower():
            partidas_usuario.append(partida)

    print("\n========== HISTORIAL ==========")

    if len(partidas_usuario) == 0:

        print(
            "No existen partidas registradas."
        )

        return

    for numero, partida in enumerate(
        partidas_usuario,
        start=1
    ):

        print(
            f"\nPARTIDA #{numero}"
        )

        print(
            f"Dificultad: {partida['dificultad']}"
        )

        print(
            f"Nivel alcanzado: {partida['nivel']}"
        )

        print(
            f"Puerta alcanzada: {partida['puerta']}"
        )

        print(
            f"Resultado: {partida['resultado']}"
        )

        print(
            f"Puntaje final: {partida['puntaje_final']}"
        )

        print("-" * 30)