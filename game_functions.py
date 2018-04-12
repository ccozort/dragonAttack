import sys

import pygame

import math

#this is a comment to test git

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move ship to right
        ship.moving_right = True
        print("event k right is listening")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print("event k left is listening")
    elif event.key == pygame.K_SPACE:
        # create new bullet and add to group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        print("bullet key event is working dogg")
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
    #respond to keystrokes
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship, bullets):
    #Update images and flip to new screen
       
    #redraw each loop
    screen.fill(ai_settings.bg_color)
    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    # update bullet position and get rid of old bullets
    bullets.update()

    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)