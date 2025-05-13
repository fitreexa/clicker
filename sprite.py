import pygame
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imaged, x, y, sizex, sizey,speed):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(imaged), (sizex, sizey)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.speed=speed
    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)