# =====================================
# CONFIGURACION GENERAL DEL JUEGO
# =====================================

# Animales base
ANIMALES = {
    "Gato": 10,
    "Leon": -30,
    "Lobo": -20,
    "Panda": 20,
    "Tigre": -30,
    "Gallina Dorada": 50
}


# =====================================
# NIVELES
# =====================================

NIVELES = {
    1: {
        "nombre": "Nivel 1",
        "puertas": 5
    },

    2: {
        "nombre": "Nivel 2",
        "puertas": 10
    },

    3: {
        "nombre": "Nivel 3",
        "puertas": 15
    }
}


# =====================================
# DIFICULTADES
# =====================================

DIFICULTADES = {

    1: {
        "nombre": "Facil",

        # puntos iniciales
        "puntaje_inicial": 10,

        # multiplicadores
        "positivo": 1,
        "negativo": 1,

        # dragon
        "dragon": 100
    },

    2: {
        "nombre": "Intermedio",

        # puntos iniciales
        "puntaje_inicial": 20,

        # positivos x1.5
        "positivo": 1.5,

        # negativos x2
        "negativo": 2,

        # dragon
        "dragon": 180
    },

    3: {
        "nombre": "Dificil",

        # puntos iniciales
        "puntaje_inicial": 30,

        # positivos x2
        "positivo": 2,

        # negativos x3
        "negativo": 3,

        # dragon
        "dragon": 300
    }
}