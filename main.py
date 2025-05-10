import pygame
import sys
from helper import resource_path
from sprite import GameSprite

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")
background = pygame.image.load(resource_path("assets/main_pole.jpg"))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

asset=resource_path("assets/cube1.jpg")
button = GameSprite(asset,200, 200, 220, 220)

clicks = 0
font = pygame.font.SysFont("Arial", 36)
game = True
while game:
    screen.blit(background, (0, 0))
    button.reset(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.collidepoint(event.pos):
                    clicks += 1
    
    text = font.render(f"Кликов: {clicks}", True, BLACK)
    screen.blit(text, (10,10))
    pygame.display.flip()

pygame.quit()
sys.exit()