import pygame
import sys
from helper import resource_path
from sprite import GameSprite

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")
background = pygame.image.load(resource_path("assets/main_pole.jpg"))

WHITE = (0, 128, 0)

asset=resource_path("assets/cube1.jpg")
asset1=resource_path("assets/bul.png")
button = GameSprite(asset,175, 200, 220, 220)
dub=GameSprite(asset1,590, 50, 120, 120)
transparent_surface = pygame.Surface((400, 800), pygame.SRCALPHA) 
transparent_surface.fill((119, 136, 153, 128))

clicks = 0
font = pygame.font.SysFont("Arial", 50)
game = True
while game:
    screen.blit(background, (0, 0))
    screen.blit(transparent_surface, (500, 0))
    dub.reset(screen)
    button.reset(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.collidepoint(event.pos):
                    clicks += 1
                    button.rect.y +=10 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if button.collidepoint(event.pos):
                    button.rect.y -= 10
    
    text = font.render(f"Кликов: {clicks}", True, WHITE)
    screen.blit(text, (10,10))
    pygame.display.flip()

pygame.quit()
sys.exit()
