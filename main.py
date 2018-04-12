'''
I AM TOTALLY STEALING THIS FROM PYTHON CRASH COURSE ALIEN Invasion AND THEN MODIFYING TO USE MEDIEVAL SPRITES AND INCLUDE HITPOINTS AND POWER UPS

'''
#week 1 got ship to show up on screen
#week 2 got ship to fire bullets
#week 3 got bullets to die when off screen
#this week i included removing bullet from memory and incorporating update function, all from python crash course
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
        gf.update_bullets(bullets)
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