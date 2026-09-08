from avatar import (
    registrar_usuario,
    iniciar_sesion,
    eliminar_usuario
)

from menu import (
    menu_principal,
    menu_dificultad,
    menu_partida_guardada,
    mostrar_reglas
)

from reporte import (
    cargar_progreso,
    mostrar_historial
)

from juego import jugar


usuario_actual = None


while True:

    menu_principal()

    try:

        opcion = int(
            input("Seleccione una opción: ")
        )

        # REGISTRAR

        if opcion == 1:

            registrar_usuario()

        # LOGIN

        elif opcion == 2:

            usuario = iniciar_sesion()

            if usuario:

                usuario_actual = usuario

        # REGLAS

        elif opcion == 3:

            mostrar_reglas()

        # JUGAR

        elif opcion == 4:

            if not usuario_actual:

                print(
                    "\nDebe iniciar sesión primero."
                )

                continue

            progreso = cargar_progreso()

            if (
                progreso
                and progreso["apodo"]
                == usuario_actual["apodo"]
            ):

                menu_partida_guardada()

                try:

                    opcion_partida = int(
                        input(
                            "Seleccione una opción: "
                        )
                    )

                except ValueError:

                    print(
                        "Opción inválida."
                    )

                    continue

                if opcion_partida == 1:

                    jugar(
                        usuario_actual,
                        progreso["dificultad"],
                        progreso
                    )

                elif opcion_partida == 2:

                    menu_dificultad()

                    try:

                        dificultad = int(
                            input(
                                "Seleccione dificultad: "
                            )
                        )

                    except ValueError:

                        print(
                            "Valor inválido."
                        )

                        continue

                    if dificultad not in [1, 2, 3]:

                        print(
                            "Dificultad inválida."
                        )

                        continue

                    jugar(
                        usuario_actual,
                        dificultad
                    )

                else:

                    print(
                        "Opción inválida."
                    )

            else:

                menu_dificultad()

                try:

                    dificultad = int(
                        input(
                            "Seleccione dificultad: "
                        )
                    )

                except ValueError:

                    print(
                        "Valor inválido."
                    )

                    continue

                if dificultad not in [1, 2, 3]:

                    print(
                        "Dificultad inválida."
                    )

                    continue

                jugar(
                    usuario_actual,
                    dificultad
                )

        # HISTORIAL

        elif opcion == 5:

            if not usuario_actual:

                print(
                    "\nDebe iniciar sesión primero."
                )

                continue

            mostrar_historial(
                usuario_actual["apodo"]
            )

        # ELIMINAR USUARIO

        elif opcion == 6:

            eliminar_usuario()

            if usuario_actual:

                usuario_actual = None

        # SALIR

        elif opcion == 7:

            print(
                "\nGracias por jugar Dragon King."
            )

            break

        else:

            print(
                "\nOpción inválida."
            )

    except ValueError:

        print(
            "\nDebe ingresar un número."
        )