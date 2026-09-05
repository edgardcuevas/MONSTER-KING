import random



puntaje = 10

# Listas con las puertas de cada nivel.
nivel1 = [1, 2, 3, 4, 5]
nivel2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nivel3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


animales = ["Gato", "Leon", "Lobo", "Panda", "Tigre", "gallina-dorada"]


print("JUEGO DE PUERTAS")
print("Comienzas con", puntaje, "puntos.")


juego_terminado = False


for numero_nivel, puertas in [(1, nivel1), (2, nivel2), (3, nivel3)]:
	print("\nComienza el Nivel", numero_nivel)

	for puerta in puertas:
		input("Presiona ENTER para abrir la puerta " + str(puerta) + ": ")

		if numero_nivel == 3 and puerta == 14:
			animal = "Dragon"
			cambio = -100
		elif numero_nivel == 3 and puerta == 15:
			animal = "Princesa"
		else:
			animal = random.choice(animales)

		if animal == "Gato":
			cambio = 10
		elif animal == "Leon":
			cambio = -30
		elif animal == "Lobo":
			cambio = -20
		elif animal == "Panda":
			cambio = 20
		elif animal == "Tigre":
			cambio = -30
		elif animal == "gallina-dorada":
			cambio = 50
		else:
			cambio = 0

		puntaje = puntaje + cambio
		print("Puerta", puerta)
		print("Aparecio:", animal)
		print("Puntos ganados o perdidos:", cambio)
		print("Puntaje actual:", puntaje)

		if puntaje <= 0:
			print("Losiento mucho, mejor suerte la próxima vez.")
			juego_terminado = True
			break

	if juego_terminado:
		break

if juego_terminado:
	print("Puntaje final:", puntaje)
else:
	print("\nTerminaste el juego.")
	print("Felicidades, has rescatado a la princesa.")
	print("Puntaje final:", puntaje)
