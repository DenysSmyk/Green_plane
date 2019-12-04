import pygame
from pygame.sprite import Sprite


class Bird_4(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen

        self.image = pygame.image.load("images/birds/bird_4.png")
        self.image=pygame.transform.scale(self.image,(90,100))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.x=self.screen_rect.x+12000
        self.rect.y = self.screen_rect.y + 650

        self.moving_left=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx-=0.25
