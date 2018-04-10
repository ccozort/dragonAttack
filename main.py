''' i want to use the python crash course example for space invaders
I can write a recipe for brownies in here with no 

'''
import pygame
import sys
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
    #initialize pygame, settings, and screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #initialize
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #set background color 
    bg_color = (230, 230, 230)
    #CREATE A SHIP  
    ship = Ship(ai_settings, screen)
    # make a group to store bullets
    bullets = Group()
    
    #Start the main loop for the run_game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # get rid of offscreen bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
        #Watch for keyboard and mouse events
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #redraw screen each pass through the loop
        # screen.fill(ai_settings.bg_color)    
        #Redraw ship each pass through loop
        # ship.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()