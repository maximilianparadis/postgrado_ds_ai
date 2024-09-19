import pygame
import math
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Red Estrella")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clase para representar un nodo (computadora)
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = BLUE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Clase para representar un paquete de datos
class Packet:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.pos = list(start)
        self.speed = 5
        self.color = RED

    def move(self):
        dx = self.end[0] - self.pos[0]
        dy = self.end[1] - self.pos[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > self.speed:
            self.pos[0] += (dx / distance) * self.speed
            self.pos[1] += (dy / distance) * self.speed
        else:
            self.pos = list(self.end)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), 5)

# Crear nodos
center_node = Node(WIDTH // 2, HEIGHT // 2)
nodes = [Node(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)) for _ in range(5)]

packets = []

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Dibujar conexiones
    for node in nodes:
        pygame.draw.line(screen, BLACK, (center_node.x, center_node.y), (node.x, node.y))

    # Dibujar nodos
    center_node.draw(screen)
    for node in nodes:
        node.draw(screen)

    # Generar nuevos paquetes aleatoriamente
    if random.random() < 0.02:
        start_node = random.choice(nodes)
        end_node = random.choice(nodes)
        if start_node != end_node:
            packets.append(Packet((start_node.x, start_node.y), (center_node.x, center_node.y)))
            packets.append(Packet((center_node.x, center_node.y), (end_node.x, end_node.y)))

    # Mover y dibujar paquetes
    for packet in packets[:]:
        packet.move()
        packet.draw(screen)
        if packet.pos == list(packet.end):
            packets.remove(packet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
