import pygame
pygame.init()

width, height = 500, 500
fps = 40
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumper")

class GameSprite:
    def __init__(self,x,y,w,h,image):
        self.rect = pygame.Rect(x,y,w,h)
        image = pygame.transform.scale(image, (w,h))
        self.image = image

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Pers(GameSprite):
    def __init__(self,x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed

    
    def move(self, key_left, key_right):
        k = pygame.key.get_pressed()
        if k[key_right]:
            if self.rect.right <= width:
                self.rect.x += self.speed
        elif k[key_left]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
    def jump(self):

