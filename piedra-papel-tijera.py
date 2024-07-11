def juego_ppt():
    opciones = ["piedra", "papel", "tijera"]

    jugador1 = input("Hola jugador1, ¿qué eliges? Piedra, Papel o Tijera? ").lower()
    while jugador1 not in opciones:
        jugador1 = input("Opción inválida. Introduce Piedra, Papel o Tijera: ").lower()

    jugador2 = input("Hola jugador2, ¿qué eliges? Piedra, Papel o Tijera? ").lower()
    while jugador2 not in opciones:
        jugador2 = input("Opción inválida. Introduce Piedra, Papel o Tijera: ").lower()

    # No necesitas un tercer jugador, asumo que fue un error
    # jugador3 = input("Hola jugador3, ¿qué eliges? Piedra, Papel o Tijera? ")

    if jugador1 == jugador2:
        print("Ha sido un empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Ha ganado el jugador1")
    else:
        print("Ha ganado el jugador2")

juego_ppt()