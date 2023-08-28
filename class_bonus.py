from game_object import objects
import pygame as pg

from framedraw import window, imgBrick, imgTanks, imgBonuses, sndStar, sndLive



class Bonus:
    def __init__(self, px, py, bonusNum):
        objects.append(self)
        self.type = 'bonus'

        self.image = imgBonuses[bonusNum]
        self.rect = self.image.get_rect(center = (px, py))

        self.timer = 600
        self.bonusNum = bonusNum

    def update(self):
        if self.timer > 0: self.timer -= 1
        else: objects.remove(self)

        for obj in objects:
            if obj.type == 'tank' and self.rect.colliderect(obj.rect):
                if self.bonusNum == 0:
                    if obj.rank < len(imgTanks) - 1:
                        obj.rank += 1
                        objects.remove(self)
                        sndStar.play()
                        break
                elif self.bonusNum == 1:
                    obj.hp += 1
                    objects.remove(self)
                    sndLive.play()
                    break

    def draw(self):
        if self.timer % 30 < 15:
            window.blit(self.image, self.rect)