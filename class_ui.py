import pygame as pg
from game_object import objects
from framedraw import window, WIDTH, HEIGHT, TILE

fontUI = pg.font.Font(None,32)
fontBig = pg.font.Font(None, 70)

class UI:
    def __init__(self):
        pass
    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pg.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.rank), 1, 'black')
                rect = text.get_rect(center=(5 + i * 70 + 11, 5 + 11))
                window.blit(text, rect)

                text = fontUI.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + TILE, 5 + 11))
                window.blit(text, rect)
                i += 1
        t = 0
        for obj in objects:
            if obj.type == 'tank':
                t += 1
                tankWin = obj

        if t == 1:
            text = fontBig.render('ПОБЕДИЛ', 1, 'white')
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
            window.blit(text, rect)

            pg.draw.rect(window, tankWin.color, (WIDTH // 2 - 100, HEIGHT // 2, 200, 200))
