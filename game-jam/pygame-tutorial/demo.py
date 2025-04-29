import pygame
import sys

pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mitt første spill!")

# Clock for framerate
clock = pygame.time.Clock()
FPS = 60

# colors
WHITE = (255,255,255)
BLUE = (60,60,255)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
sys.exit()