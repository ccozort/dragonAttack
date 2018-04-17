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
from turret import Turret
from enemy import Enemy

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
    turret = Turret(ai_settings, screen, ship)
    # make a group to store bullets
    bullets = Group()
    enemies = Group()
    # create fleet

    gf.create_fleet(ai_settings, screen, enemies)

    # make an enemy
    enemy = Enemy(ai_settings, screen)
    
    #Start the main loop for the run_game
    while True:
        gf.check_events(ai_settings, screen, ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, enemies, bullets)
        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()