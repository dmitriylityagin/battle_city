import pygame as pg
from pygame.time import Clock

WIDTH, HEIGHT = 800, 600
TILE = 42
FPS = 60

window = pg.display.set_mode((800, 600))
pg.init()


imgBrick = pg.image.load('images/block_brick.png')
imgTanks = [
    pg.image.load('images/tank1.png'),
    pg.image.load('images/tank2.png'),
    pg.image.load('images/tank3.png'),
    pg.image.load('images/tank4.png'),
    pg.image.load('images/tank5.png'),
    pg.image.load('images/tank6.png'),
    pg.image.load('images/tank7.png'),
    pg.image.load('images/tank8.png'),
    ]
imgBangs = [
    pg.image.load('images/bang1.png'),
    pg.image.load('images/bang2.png'),
    pg.image.load('images/bang3.png'),
    ]





