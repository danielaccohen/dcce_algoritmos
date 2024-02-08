import random

# Batalla
PS_jugador = 100  # Puntos de Salud del Jugador
PS_oponente = 100  # Puntos de Salud del Oponente
defensa_oponente = 100
defensa_jugador = 100

def ataque_malicioso(PS, defensa):
    nueva_defensa = max(1, defensa - 10)
    return (PS, nueva_defensa)

def ataque_placaje(PS, defensa):
    nueva_PS = PS - 35 / (defensa / 100)
    return (nueva_PS, defensa)

def ataque_ascuas(PS, defensa):
    nueva_PS = PS - 20
    return (nueva_PS, defensa)

def ataque_oponente(PS, defensa):
    ataque = random.randrange(1, 3 + 1)
    if ataque == 1:  # látigo
        nueva_defensa = max(1, defensa - 10)
        return (PS, nueva_defensa)
    elif ataque == 2:  # placaje
        nueva_PS = PS - 35 * (100 / defensa)
        return (nueva_PS, defensa)
    elif ataque == 3:  # pistola de agua
        nueva_PS = PS - 40
        return (nueva_PS, defensa)

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("Ataque? (opciones disponibles: malicioso, placaje y ascuas) ")
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == "malicioso":
        PS_jugador, defensa_oponente = ataque_malicioso(PS_jugador, defensa_oponente)
    elif ataque_jugador == "placaje":
        PS_oponente, defensa_oponente = ataque_placaje(PS_oponente, defensa_oponente)
    elif ataque_jugador == "ascuas":
        PS_oponente, defensa_oponente = ataque_ascuas(PS_oponente, defensa_oponente)
    else:
        print("Qué estás haciendo?! tus ataques son malicioso, placaje, y ascuas")

    ataque_oponente(PS_jugador, defensa_jugador)

# Verificar el resultado de la batalla
if PS_oponente <= 0 and PS_jugador <= 0:
    print("Empate")
elif PS_oponente <= 0:
    print("Felicidades, has ganado")
else:
    print("Lo siento, has perdido")
