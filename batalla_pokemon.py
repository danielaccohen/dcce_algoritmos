import random #para decidir el ataque del oponente con randrange
#Batalla
PS_jugador = 100 #Puntos de Salud del Jugador
PS_oponente = 100 #Puntos de Salud del Oponente
defensa_oponente = 100
defensa_jugador = 100
while PS_jugador>0 and PS_oponente>0:
    ataque_jugador = input ("Ataque?(opciones disponibles: malicioso, placaje y ascuas) ")
    ataque_jugador= ataque_jugador.lower()
    if ataque_jugador=="malicioso":
        defensa_oponente = defensa_oponente-10
        if defensa_oponente<=0:
            defensa_oponente=1
    elif ataque_jugador=="placaje":
        PS_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador=="ascuas":
        PS_oponente-=20
    else:
        print("Qué estás haciendo?! tus ataques son" , "malacioso, placaje, y ascuas")
    ataque_oponente=random.randrange (1, 3+1)
    if ataque_oponente==1: #látigo
        print("El oponente uso látigo")
        defensa_jugador=-10
        if defensa_jugador<=0:
            defensa_jugador=1
    elif ataque_oponente==2:
        print("El oponente uso placaje")
        PS_jugador-=35*(100/defensa_jugador)
    elif ataque_oponente==3: #pistola de agua
        print ("El oponente uso pistola de agua")
        PS_jugador-=40
#randrange esta garantizado a ser 1, 2 ó 3
#si termina el ciclo alguien ha ganado
if PS_oponente<=0 and PS_jugador<=0:
    print("Empate")
elif PS_oponente<=0:
    print("Felicidades, has ganado")
else:
    print("Lo siento, has perdido")
quit()