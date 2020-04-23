import pygame
from data import config
from data.config import Point


class Snake(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 1
        self.yspeed = 0
        self.length = 1
        self.body = []

    def dir(self, x, y):
        # Already going Right
        if self.xspeed == 1 and self.yspeed == 0:
            if x != -1 and y != 0:
                self.xspeed = x
                self.yspeed = y

        # Already going Left
        if self.xspeed == -1 and self.yspeed == 0:
            if x != 1 and y != 0:
                self.xspeed = x
                self.yspeed = y

        # Already going Up
        if self.xspeed == 0 and self.yspeed == -1:
            if x != 0 and y != 1:
                self.xspeed = x
                self.yspeed = y

        # Already going Down
        if self.xspeed == 0 and self.yspeed == 1:
            if x != 0 and y != -1:
                self.xspeed = x
                self.yspeed = y

    def update(self):
        self.body.insert(0, Point(self.x, self.y))
        for _ in range(len(self.body) - self.length):
            self.body.pop()

        self.x += self.xspeed * config.grid_size
        self.y += self.yspeed * config.grid_size

        # Looping the snake across the screen
        if self.x > config.width - config.grid_size:
            self.x = 0
        if self.y > config.height - config.grid_size:
            self.y = 0
        if self.x < 0:
            self.x = config.width - config.grid_size
        if self.y < 0:
            self.y = config.height - config.grid_size

    def show(self, screen):
        for p in self.body:
            pygame.draw.rect(screen, (255, 255, 255), (p.x,
                                                       p.y, config.grid_size-1, config.grid_size-1))

    def eat(self, food):
        if config.distance(Point(self.x, self.y), Point(food.x, food.y)) < 2:
            self.length += 1
            return True
        return False

    def hit(self):
        if self.length > 2:
            tails = self.body[:]
            head = tails.pop(0)
            for p in tails:
                if config.distance(p, head) < 2:
                    return True
        return False

    def reborn(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 1
        self.yspeed = 0
        self.length = 1
        self.body = []

    def body_in(self, x, y):
        if self.x == x and self.y == y:
            return True
        return False
