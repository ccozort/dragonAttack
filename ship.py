import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''Init the ship and get starting pos'''
        self.screen = screen
        #load ship image
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/Falcon.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update pos based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1
        self.rect.centerx = self.center

    def blitme(self):
        # draw ship at its current location
        self.screen.blit(self.image, self.rect)