import pygame,sys
from settings import Settings
from plane import Plane
from bird_1 import Bird_1
from bird_2 import Bird_2
from bird_3 import Bird_3
from bird_4 import Bird_4
from bird_5 import Bird_5
from bird_6 import Bird_6

import game_function as g_f
from pygame.sprite import Group
from background import Background
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame import mixer



def init_game():
    pygame.init()

    game_settings = Settings()

    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    plane=Plane(screen)
    stats=GameStats(game_settings)

    bird_1 = Bird_1(screen)
    bird_2 = Bird_2(screen)
    bird_3 = Bird_3(screen)
    bird_4 = Bird_4(screen)
    bird_5 = Bird_5(screen)

    bird_6=Bird_6(screen)
    background=Background(screen)
    pygame.display.set_caption("Green Plane")


    bullets=Group()
    enemies = Group()
    enemies.add(bird_1, bird_2, bird_3, bird_4, bird_5, bird_6)
    friends=Group()
    friends.add()
    planes=Group()
    planes.add(plane)

    button = Button(screen, game_settings, "Play")
    sb = Scoreboard(game_settings, screen, stats)


    while True:
        g_f.chek_events(game_settings, plane, screen, bullets, button, stats, enemies, sb)
        g_f.update_screen(background, planes, bullets, enemies, screen, button, friends, stats, sb)



        if stats.game_active:
            g_f.update_bullets(bullets, enemies, planes, friends, bird_6, stats, sb, screen)
            g_f.aliens_move(enemies, screen, friends, planes, bullets, plane)



            plane.update()
            plane.blitme()


init_game()
