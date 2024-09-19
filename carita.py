import time

def dibujar_robot():
    robot = [
        "    ___    ",
        "   /o o\\   ",
        "  |  ^  |  ",
        "   \\_-_/   ",
        "  /|   |\\  ",
        " / |   | \\ ",
        "   |___|   ",
        "    | |    ",
        "    | |    ",
        "   /   \\   "
    ]
    return robot

def imprimir_robot(robot):
    for linea in robot:
        print(linea)

def limpiar_pantalla():
    print("\033[H\033[J", end="")

# Animación
for _ in range(4):
    robot = dibujar_robot()
    imprimir_robot(robot)
    time.sleep(0.5)
    limpiar_pantalla()

print("¡Animación terminada!")

