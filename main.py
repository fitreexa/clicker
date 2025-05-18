import pygame
import sys
from helper import resource_path
from sprite import GameSprite
# from en import Enemy
# import time

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
text_bul=win=font2.render('500 КЛИКОВ',True,(255,0,0))
text_almaz=win=font2.render('1500 КЛИКОВ',True,(255,0,0))

transparent_surface = pygame.Surface((400, 800), pygame.SRCALPHA) 
transparent_surface.fill((119, 136, 153, 128))

none=''

clicks = 0
power_of_clicks=10
first_achievement=100
second_achievement=500
third_achievement=1500
game = True
while game:
    current_time = pygame.time.get_ticks()
    screen.blit(background, (0, 0))
    screen.blit(transparent_surface, (500, 0))
    dub.reset(screen)
    button.reset(screen)
    almaz.reset(screen)
    bul.reset(screen)
    screen.blit(text_dub,(595,100))
    screen.blit(text_bul,(595,300))
    screen.blit(text_almaz,(595,500))
    # sunduk.reset(screen)
    # sunduk.auto_move(x_finish=390,x_start=-150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button.collidepoint(event.pos):
                clicks += power_of_clicks
                button.rect.y += 10
                if clicks >= first_achievement:
                    power_of_clicks = 200
                    text_dub=win=font2.render(none,True,(255,0,0))
                    screen.blit(text_dub,(595,100))
                    button.image=pygame.transform.scale(
            pygame.image.load(asset3), (220, 220)
        )
                if clicks >= second_achievement:
                    power_of_clicks = 500
                    text_bul=win=font2.render(none,True,(255,0,0))
                    screen.blit(text_bul,(595,300))
                    button.image=pygame.transform.scale(
            pygame.image.load(asset1), (220, 220)
        )
                if clicks >= third_achievement:
                    power_of_clicks = 12
                    text_almaz=win=font2.render(none,True,(255,0,0))
                    screen.blit(text_almaz,(595,500))
                    button.image=pygame.transform.scale(
            pygame.image.load(asset2), (220, 220)
        )
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if button.collidepoint(event.pos):
                    button.rect.y -= 10
    
    text = font1.render(str(clicks), True, WHITE)
        # text = font.render(f"Кликов: {clicks}", True, WHITE)
    screen.blit(text, (20,10))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()