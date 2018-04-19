import sys

import pygame

import math

#this is a comment to test git

from bullet import Bullet
from turret import Turret
from enemy import Enemy
from background import Background



black = (0,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(ai_settings, text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (ai_settings.screen_width/2, ai_settings.screen_height/2)
    screen.blit(TextSurf, TextRect)
def update_mouse():
    p = pygame.mouse.get_pos()
    return str(p)

def check_keydown_events(event, ai_settings, screen, ship,  bullets):
    if event.key == pygame.K_RIGHT:
        #move ship to right
        ship.moving_right = True
        # print("event k right is listening")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # print("event k left is listening")
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        # print("bullet key event is working dogg")

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def get_number_enemies_x(ai_settings, enemy_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * enemy_width
    number_enemies_x = int(available_space_x/(2*enemy_width))
    return number_enemies_x

def get_number_rows(ai_settings, ship_height, enemy_height):
    # determine number of rows
    available_space_y = (ai_settings.screen_height - (3 * enemy_height) - ship_height)
    number_rows = int(available_space_y /(2 * enemy_height))
    return number_rows

def create_enemy(ai_settings, screen, enemies, enemy_number, row_number):
    """create an alien and place it in the row"""
    enemy = Enemy(ai_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
    enemies.add(enemy)

def create_fleet(ai_settings, screen, ship, enemies):
    # create a fleet of enemies
    # create an enemy and find the number of enemies in a row
    # spacing between enemies is equal to one enemy width
    enemy = Enemy(ai_settings, screen)
    number_enemies_x = get_number_enemies_x(ai_settings, enemy.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, enemy.rect.height)

    # create fleet of enemies
    for row_number in range(number_rows):
        for enemy_number in range(number_enemies_x):
            create_enemy(ai_settings, screen, enemies, enemy_number, row_number)

def fire_bullet(ai_settings, screen, ship, bullets):
    # create new bullet and add to group
    print(len(bullets))
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    # update bullet position and get rid of old bullets
    bullets.update()
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_events(ai_settings, screen, ship, bullets):
    #respond to keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def loadify(img):
    return pygame.image.load(img).convert_alpha()
def update_background()    
def update_screen(ai_settings, screen, ship, enemies, bullets):
    #Update images and flip to new screen
    #redraw each loop
    # screen.fill(ai_settings.bg_color)
    
    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #draw turret
    t = Turret(ai_settings,screen,ship)
    t.draw_turret()
    enemies.draw(screen)
    # enemy.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()

