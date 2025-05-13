from sprite import GameSprite
class Enemy(GameSprite):
    def __init__(self,imaged,x,y,sizex,sizey,speed):
        super().__init__(imaged,x,y,sizex,sizey,speed)
        self.directory='right'
    def auto_move(self,x_start,x_finish):
        if self.rect.x <= x_start:
            self.directory = 'right'
        elif self.rect.x >= x_finish:
            self.directory = 'left'
        
        if self.directory == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        #      if self.directory == 'left':
        #     self.rect.x -= self.speed
        # else:
        #     self.rect.x += self.speed
    
    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))