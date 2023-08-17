from game_object import objects
import pygame as pg

from framedraw import window


class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'
        self.rect = pg.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        pg.draw.rect(window, 'green', self.rect)
        pg.draw.rect(window, 'gray20', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)
