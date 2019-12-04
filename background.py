import pygame

class Background():
    def __init__(self,screen):
        self.screen=screen
        self.bg_img=pygame.image.load("images/BG_green_plane.png")
        self.bg_img = pygame.transform.scale(self.bg_img, (1500,1000))
        self.rect_img=self.bg_img.get_rect()
        self.bg_speed=2
        self.bg_x1=0
        self.bg_x2=self.rect_img.width

    def update(self):
        self.bg_x1-=self.bg_speed
        self.bg_x2-=self.bg_speed

        if self.bg_x1<= -self.rect_img.width:
            self.bg_x1=self.rect_img.width

        if self.bg_x2<=-self.rect_img.width:
            self.bg_x2=self.rect_img.width

        self.screen.blit(self.bg_img,(self.bg_x1, 0))
        self.screen.blit(self.bg_img,(self.bg_x2, 0))