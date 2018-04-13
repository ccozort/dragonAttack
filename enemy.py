import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    # a class to represent an enemy ship

    def __init__(self, ai_settings, screen):
        # init the alien and set its starting pos
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load('images/tie.png')
        self.rect = self.image.get_rect()

        # start each enemy at the top left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # draw alien at its current location
        self.screen.blit(self.image, self.rect)
