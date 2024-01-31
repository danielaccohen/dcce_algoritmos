import random

# Batalla
jugador = (100, 100)  # Tupla que almacena los puntos de salud y defensa del Jugador
oponente = (100, 100)  # Tupla que almacena los puntos de salud y defensa del Oponente

ataques_jugador = {}  # Almacenar ataques del jugador en un diccionario
ataques_oponente = {}  # Almacenar ataques del oponente en un diccionario

while jugador[0] > 0 and oponente[0] > 0:
    ataque_jugador = input("Ataque? (opciones disponibles: malicioso, placaje y ascuas) ")
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == "malicioso":
        oponente = (oponente[0], max(1, oponente[1] - 10))
    elif ataque_jugador == "placaje":
        resta_salud = 35 / (oponente[1] / 100)
        oponente = (oponente[0] - resta_salud, max(1, oponente[1] - 10))
    elif ataque_jugador == "ascuas":
        oponente = (oponente[0] - 20, oponente[1])
    else:
        print("Qué estás haciendo?! tus ataques son malicioso, placaje, y ascuas")

    # Contar la frecuencia de ataques del jugador
    ataques_jugador[ataque_jugador] = ataques_jugador.get(ataque_jugador, 0) + 1

    ataque_oponente = random.randrange(1, 3 + 1)
    if ataque_oponente == 1:  # látigo
        print("El oponente uso látigo")
        jugador = (jugador[0] - 10, max(1, jugador[1] - 10))
    elif ataque_oponente == 2:
        print("El oponente uso placaje")
        resta_salud = 35 * (100 / jugador[1])
        jugador = (jugador[0] - resta_salud, max(1, jugador[1] - 10))
    elif ataque_oponente == 3:  # pistola de agua
        print("El oponente uso pistola de agua")
        jugador = (jugador[0] - 40, jugador[1])

    # Contar la frecuencia de ataques del oponente
    ataques_oponente[ataque_oponente] = ataques_oponente.get(ataque_oponente, 0) + 1

# Mostrar ataques almacenados
print("\nFrecuencia de ataques del jugador:", ataques_jugador)
print("Frecuencia de ataques del oponente:", ataques_oponente)

# Verificar el resultado de la batalla
if oponente[0] <= 0 and jugador[0] <= 0:
    print("Empate")
elif oponente[0] <= 0:
    print("Felicidades, has ganado")
else:
    print("Lo siento, has perdido")
