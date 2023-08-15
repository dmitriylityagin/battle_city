import pygame as pg
from framedraw import WIDTH, HEIGHT, window
from game_object import objects

bullets = []


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.window = window
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.objects = objects
    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in self.objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break

    def draw(self):
        pg.draw.circle(self.window, 'yellow', (self.px, self.py), 2)
