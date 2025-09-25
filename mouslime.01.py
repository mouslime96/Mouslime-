import pygame
import sys
import random
import math

# Initialisation
pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation complexe - Kamil")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("arialblack", 60)

# Couleurs
BLACK = (5, 5, 15)
NEON_BLUE = (50, 200, 255)
NEON_PINK = (255, 100, 200)
NEON_GREEN = (100, 255, 180)
COLORS = [NEON_BLUE, NEON_PINK, NEON_GREEN]

# Classe particule
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(2, 5)
        self.color = random.choice(COLORS)
        self.angle = random.uniform(0, math.pi * 2)
        self.speed = random.uniform(1, 3)
        self.amplitude = random.randint(20, 80)
        self.life = random.randint(80, 200)

    def update(self):
        # mouvement sinusoïdal + chute légère
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + 0.5
        self.angle += 0.05
        self.life -= 1

        # reset si mort
        if self.life <= 0 or self.y > HEIGHT:
            self.__init__()

    def draw(self, surface):
        glow = pygame.Surface((self.radius*4, self.radius*4), pygame.SRCALPHA)
        pygame.draw.circle(glow, (*self.color, 80), (self.radius*2, self.radius*2), self.radius*2)
        surface.blit(glow, (self.x - self.radius*2, self.y - self.radius*2))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Générer des particules
particles = [Particle() for _ in range(100)]

# Effet texte néon
def draw_neon_text(surface, text, pos, color):
    text_surface = FONT.render(text, True, color)
    # effet glow
    for i in range(1, 6):
        glow = FONT.render(text, True, (*color, 40))
        surface.blit(glow, (pos[0] - i, pos[1] - i))
        surface.blit(glow, (pos[0] + i, pos[1] + i))
    surface.blit(text_surface, pos)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Particules
    for p in particles:
        p.update()
        p.draw(screen)

    # Texte néon central
    draw_neon_text(screen, "KAMIL", (WIDTH//2 - 120, HEIGHT//2 - 40), NEON_BLUE)

    pygame.display.flip()
    clock.tick(60)