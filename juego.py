import random

from ascii_art import *
from datos import ANIMALES, DIFICULTADES, NIVELES
from reporte import (
    guardar_progreso,
    guardar_historial_partida,
    eliminar_progreso
)


def obtener_cambio(base, dificultad):

    if base > 0:

        return int(
            base * DIFICULTADES[dificultad]["positivo"]
        )

    return int(
        base * DIFICULTADES[dificultad]["negativo"]
    )


def mostrar_animal(nombre):

    if nombre == "Gato":
        gato()

    elif nombre == "Leon":
        leon()

    elif nombre == "Lobo":
        lobo()

    elif nombre == "Panda":
        panda()

    elif nombre == "Tigre":
        tigre()

    elif nombre == "Gallina Dorada":
        gallina_dorada()


def guardar_estado(
    usuario,
    dificultad,
    nivel,
    puerta,
    puntaje
):

    progreso = {
        "apodo": usuario["apodo"],
        "dificultad": dificultad,
        "nivel": nivel,
        "puerta": puerta,
        "puntaje": puntaje
    }

    guardar_progreso(progreso)


def registrar_resultado(
    usuario,
    dificultad,
    nivel,
    puerta,
    puntaje,
    resultado
):

    partida = {
        "apodo": usuario["apodo"],
        "dificultad":
            DIFICULTADES[dificultad]["nombre"],
        "nivel": nivel,
        "puerta": puerta,
        "resultado": resultado,
        "puntaje_final": puntaje
    }

    guardar_historial_partida(partida)


def jugar(
    usuario,
    dificultad,
    progreso=None
):

    if progreso:

        puntaje = progreso["puntaje"]
        nivel_inicial = progreso["nivel"]
        puerta_inicial = progreso["puerta"] + 1

    else:

        puntaje = DIFICULTADES[dificultad][
            "puntaje_inicial"
        ]

        nivel_inicial = 1
        puerta_inicial = 1

    print(
        f"\nPuntaje inicial: {puntaje}"
    )

    for nivel in range(
        nivel_inicial,
        4
    ):

        print(
            f"\n========== NIVEL {nivel} =========="
        )

        total_puertas = NIVELES[nivel]["puertas"]

        inicio = puerta_inicial

        if nivel != nivel_inicial:
            inicio = 1

        for puerta_actual in range(
            inicio,
            total_puertas + 1
        ):

            print(
                f"\nPuerta {puerta_actual}"
            )

            puerta()

            input(
                "Presione ENTER para abrir..."
            )

            # DRAGON

            if (
                nivel == 3
                and puerta_actual == 14
            ):

                print(
                    "\n¡¡¡HA APARECIDO EL DRAGÓN!!!"
                )

                dragon()

                danio_dragon = (
                    DIFICULTADES[dificultad][
                        "dragon"
                    ]
                )

                puntaje -= danio_dragon

                print(
                    f"\nEl dragón te quitó "
                    f"{danio_dragon} puntos."
                )

                print(
                    f"Puntaje actual: {puntaje}"
                )

                guardar_estado(
                    usuario,
                    dificultad,
                    nivel,
                    puerta_actual,
                    puntaje
                )

                if puntaje <= 0:

                    print(
                        "\nGAME OVER"
                    )

                    registrar_resultado(
                        usuario,
                        dificultad,
                        nivel,
                        puerta_actual,
                        puntaje,
                        "Derrota"
                    )

                    eliminar_progreso()

                    return

                continue

            # PRINCESA

            if (
                nivel == 3
                and puerta_actual == 15
            ):

                princesa()

                print(
                    "\n¡¡FELICIDADES!!"
                )

                print(
                    "Has rescatado a la princesa."
                )

                print(
                    f"Puntaje final: {puntaje}"
                )

                registrar_resultado(
                    usuario,
                    dificultad,
                    nivel,
                    puerta_actual,
                    puntaje,
                    "Victoria"
                )

                eliminar_progreso()

                return

            # ANIMAL ALEATORIO

            animal = random.choice(
                list(ANIMALES.keys())
            )

            valor_base = ANIMALES[animal]

            cambio = obtener_cambio(
                valor_base,
                dificultad
            )

            print(
                f"\nApareció: {animal}"
            )

            mostrar_animal(animal)

            print(
                f"Cambio de puntos: {cambio}"
            )

            puntaje += cambio

            print(
                f"Puntaje actual: {puntaje}"
            )

            guardar_estado(
                usuario,
                dificultad,
                nivel,
                puerta_actual,
                puntaje
            )

            if puntaje <= 0:

                print(
                    "\nHas perdido la partida."
                )

                registrar_resultado(
                    usuario,
                    dificultad,
                    nivel,
                    puerta_actual,
                    puntaje,
                    "Derrota"
                )

                eliminar_progreso()

                return

        print(
            f"\nNivel {nivel} completado."
        )

    eliminar_progreso()