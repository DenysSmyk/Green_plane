import pygame, sys
from bullet import Bullet
from bird_1 import Bird_1
from bird_6 import Bird_6
from pygame import mixer



def chek_events(game_settings, plane, screen, bullets, button, stats, enemies, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:

                plane.moving_right=True
            if event.key==pygame.K_LEFT:
                plane.moving_left = True

            if event.key==pygame.K_UP:
                plane.moving_up=True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key==pygame.K_DOWN:
                plane.moving_down=True
            if event.key==pygame.K_SPACE:
                plane.image = pygame.transform.scale(pygame.image.load("images/Plane/Shoot (1).png"), (300, 200))
                if len(bullets) < 50:
                    new_bullets=Bullet(game_settings,plane,screen)
                    bullets.add(new_bullets)
                bullet_Sound = mixer.Sound('music/bullet_sound.wav')
                bullet_Sound.play()
        if event.type == pygame.KEYUP:
            plane.image = pygame.transform.scale(pygame.image.load("images/Plane/Fly (1).png"), (300, 200))



            if event.key == pygame.K_RIGHT:
                plane.moving_right = False

            if event.key == pygame.K_LEFT:
                plane.moving_left = False

            if event.key==pygame.K_UP:
                plane.moving_up=False
            if event.key==pygame.K_DOWN:
                plane.moving_down=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(button, mouse_x, mouse_y, stats, bullets, plane, game_settings, screen, enemies, sb)

def check_play_button(button, mouse_x, mouse_y, stats, bullets, plane, game_settings, screen, enemies, sb):
    if button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        stats.score = 0
        sb.prep_score()
        if stats.game_over == True:
            create_enemies(screen, enemies)
        stats.game_over = False

        #aliens.empty()
        bullets.empty()
        #create_fleet(game_settings, screen, plane)
        #ship.center_ship()
        stats.reset_stats()
        # game_settings.reset_speed()
        stats.score = 0

def create_enemies(screen, enemies):
    bird_1 = Bird_1(screen)
    bird_6 = Bird_6(screen)
    enemies.add(bird_1, bird_6)


def update_screen(background, planes, bullets, enemies, screen, button, friends,stats,sb):
    pygame.display.flip()
    background.update()

    if stats.game_active == False:
        button.draw_button()
        if stats.game_over:
            screen.blit(pygame.image.load("images/game_over.png"), (0, 0))
    sb.show_score()

def aliens_move(enemies, screen, friends, planes, bullets, plane):
    enemies.draw(screen)
    for enemy in enemies.copy():
        enemy.rect.x -=3
    for friend in friends.copy():
        friend.rect.x +=1


    friends.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()




def update_bullets(bullets, enemies, plane, friends, hook, stats, sb, screen):
    bullets.update()
    # print(len(enemies))

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullets)


    if stats.enemies_life > 0 and pygame.sprite.groupcollide(enemies, bullets, False, True):
        stats.enemies_life -= 1
        sb.prep_score()

    elif stats.enemies_life == 0 and pygame.sprite.groupcollide(enemies, bullets, False, False):
        for bullet in bullets.copy():
            if pygame.sprite.collide_rect(bullet, hook):
                stats.game_active = False
                stats.game_over = True
        pygame.sprite.groupcollide(enemies, bullets, True, True)
        stats.score += 1
        score_Sound = mixer.Sound('music/score_sound.wav')
        score_Sound.play()
        stats.enemies_life = stats.score
        sb.prep_score()

    if pygame.sprite.groupcollide(enemies, plane, True, True):
        stats.game_active = False
        stats.game_over = True
    #if len(enemies) == 0

