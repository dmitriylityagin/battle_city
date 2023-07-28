import pygame as pg
from class_bullets import Bullet

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
objects = []
TILE = 32
WIDTH, HEIGHT = 800, 600
window = pg.display.set_mode((800, 600))


class Tank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pg.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]
        self.window = pg.display.set_mode((800, 600))

    def update(self):
        keys = pg.key.get_pressed()
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2
        elif keys[self.keySHOT]:
            Bullet(self,self.rect.x, self.rect.y, 100, 100, 25)

    def draw(self):
        pg.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pg.draw.line(window, 'white', self.rect.center, (x, y), 4)
