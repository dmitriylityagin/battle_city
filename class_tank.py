import json

import pygame as pg
from framedraw import window, TILE, imgTanks, HEIGHT, WIDTH, sndDead, score_red, score_blue, score, f
from game_object import objects
from class_bullets import Bullet

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Tank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pg.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1
        self.isMove = False

        self.rank = 0
        self.image = pg.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.image = pg.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pg.transform.scale(self.image, (TILE, TILE))
        self.image = pg.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))

        oldX, oldY = self.rect.topleft
        keys = pg.key.get_pressed()
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
            self.isMove = True
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
            self.isMove = True
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
            self.isMove = True
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2
            self.isMove = True
        else:
            self.isMove = False
        # bounds
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.y > HEIGHT - (TILE - 5): self.rect.y = HEIGHT - (TILE - 5)
        if self.rect.x < 0: self.rect.x = 0
        if self.rect.x > WIDTH - (TILE - 5): self.rect.x = WIDTH - (TILE - 5)

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):

        window.blit(self.image, self.rect)

    def damage(self, value):
        a = {}
        score_r = score_red
        score_b = score_blue
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
            print(self.color, 'dead')
            if self.color == 'red':
                score_b += 1
            else:
                score_r += 1
            print(score_b)
            print(score_r)
            scor = str(score).split(' ')
            scor[1] = str(score_r)
            scor[3] = str(score_b)
            a['red'] = scor[1]
            a['blue'] = scor[3]
            print(a)
            b = json.dumps(a)
            with open("score.json", "w") as outfile:
                outfile.write(b)
            f.close()
            sndDead.play()
