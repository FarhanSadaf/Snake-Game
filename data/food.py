import pygame
from data import config


class Food(object):
    def __init__(self, position=(0, 0)):
        self.x = position[0]
        self.y = position[1]

    def show(self, screen):
        pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y,
                                                 config.grid_size, config.grid_size))

    def change_location(self, position):
        self.x = position[0]
        self.y = position[1]
