import pygame
import sys
from helper import resource_path
from sprite import GameSprite
from en import Enemy

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")
background = pygame.image.load(resource_path("assets/main_pole.jpg"))
font1 = pygame.font.SysFont("Arial", 55)
font2= pygame.font.SysFont("San Francisco Pro V@ri@ble", 25)

WHITE = (0, 128, 0)

asset=resource_path("assets/cube1.jpg")
asset1=resource_path("assets/bul.png")
asset2=resource_path("assets/almaz.jpg")
asset3=resource_path("assets/dube1.jpg")
asset4=resource_path("assets/sunduk.jpg")

button = GameSprite(asset,175, 200, 220, 220,0)
dub=GameSprite(asset3,590, 50, 120, 120,0)
bul=GameSprite(asset1,590, 250, 120, 120,0)
almaz=GameSprite(asset2,590, 450, 120, 120,0)
# sunduk=Enemy(asset4,-150, 100, 120, 120,1)

text_dub=win=font2.render('100 КЛИКОВ',True,(255,0,0))
text_bul=win=font2.render('1000 КЛИКОВ',True,(255,0,0))
text_almaz=win=font2.render('5000 КЛИКОВ',True,(255,0,0))

transparent_surface = pygame.Surface((400, 800), pygame.SRCALPHA) 
transparent_surface.fill((119, 136, 153, 128))

clicks = 0
game = True
while game:
    screen.blit(background, (0, 0))
    screen.blit(transparent_surface, (500, 0))
    dub.reset(screen)
    button.reset(screen)
    almaz.reset(screen)
    bul.reset(screen)
    # sunduk.reset(screen)
    # sunduk.auto_move(x_finish=390,x_start=-150)
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
    
    text = font1.render(str(clicks), True, WHITE)
        # text = font.render(f"Кликов: {clicks}", True, WHITE)
    screen.blit(text, (20,10))
    screen.blit(text_dub,(595,100))
    screen.blit(text_bul,(590,300))
    screen.blit(text_almaz,(590,500))
    pygame.display.flip()

pygame.quit()
sys.exit()
