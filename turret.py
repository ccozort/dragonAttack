import pygame
from pygame.sprite import Sprite

class Turret(Sprite):
    # class to manage turrets
    def __init__(self, ai_settings, screen, ship):
        # create turret object
        super().__init__()
        self.screen = screen

        # create a turret
        self.rect = pygame.Rect(0,0, ai_settings.turret_width, ai_settings.turret_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.centerx
        # store turret pos as decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.turret_color

    def update(self):
        # move turret up screen
        # update decimal pos of the turret
        # self.y -= self.speed_factor
        # update rect pos
        self.rect.y = self.y
        # print("turret update is calling")
    
    def draw_turret(self):
        # draw turret on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        # print("draw turret is calling")
        