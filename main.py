import pygame
import sys
from helper import resource_path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

background = pygame.image.load(resource_path("assets/main_pole.jpg"))

clicks = 0
font = pygame.font.SysFont("Arial", 36)
game = True
while game:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicks += 1
    
    text = font.render(f"Кликов: {clicks}", True, BLACK)
    screen.blit(text, (10,10))
    pygame.display.flip()

pygame.quit()
sys.exit()