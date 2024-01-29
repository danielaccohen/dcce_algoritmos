import random

# Batalla
PS_jugador = 100  # Puntos de Salud del Jugador
PS_oponente = 100  # Puntos de Salud del Oponente
defensa_oponente = 100
defensa_jugador = 100

ataques_jugador = {}  # Almacenar ataques del jugador en un diccionario
ataques_oponente = {}  # Almacenar ataques del oponente en un diccionario

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("Ataque? (opciones disponibles: malicioso, placaje y ascuas) ")
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == "malicioso":
        defensa_oponente = max(1, defensa_oponente - 10)
    elif ataque_jugador == "placaje":
        PS_oponente -= 35 / (defensa_oponente / 100)
    elif ataque_jugador == "ascuas":
        PS_oponente -= 20
    else:
        print("Qué estás haciendo?! tus ataques son malicioso, placaje, y ascuas")

    # Contar la frecuencia de ataques del jugador
    if ataque_jugador in ataques_jugador:
        ataques_jugador[ataque_jugador] += 1
    else:
        ataques_jugador[ataque_jugador] = 1

    ataque_oponente = random.randrange(1, 3 + 1)
    if ataque_oponente == 1:  # látigo
        print("El oponente uso látigo")
        defensa_jugador = max(1, defensa_jugador - 10)
    elif ataque_oponente == 2:
        print("El oponente uso placaje")
        PS_jugador -= 35 * (100 / defensa_jugador)
    elif ataque_oponente == 3:  # pistola de agua
        print("El oponente uso pistola de agua")
        PS_jugador -= 40

    # Contar la frecuencia de ataques del oponente
    if ataque_oponente in ataques_oponente:
        ataques_oponente[ataque_oponente] += 1
    else:
        ataques_oponente[ataque_oponente] = 1

# Mostrar ataques almacenados
print("\nFrecuencia de ataques del jugador:", ataques_jugador)
print("Frecuencia de ataques del oponente:", ataques_oponente)

# Verificar el resultado de la batalla
if PS_oponente <= 0 and PS_jugador <= 0:
    print("Empate")
elif PS_oponente <= 0:
    print("Felicidades, has ganado")
else:
    print("Lo siento, has perdido")
