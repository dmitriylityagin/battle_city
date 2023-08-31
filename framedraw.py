import json
import pygame as pg
from pygame.time import Clock

WIDTH, HEIGHT = 800, 600
TILE = 42
FPS = 60
f = open('score.json')
score = json.load(f)
score1 = str(score).split(' ')
score_red = int(score1[1][1:-2])
score_blue = int(score1[3][1:-2])
print(score_red,score_blue)
window = pg.display.set_mode((800, 600))
pg.init()


bonusTimer = 180

timer = 0
isMove = False
isWin = False

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

imgBonuses = [
    pg.image.load('images/bonus_star.png'),
    pg.image.load('images/bonus_tank.png'),
    ]


sndShot = pg.mixer.Sound('sounds/shot.wav')
sndDestroy = pg.mixer.Sound('sounds/destroy.wav')
sndDead = pg.mixer.Sound('sounds/dead.wav')
sndLive = pg.mixer.Sound('sounds/live.wav')
sndStar = pg.mixer.Sound('sounds/star.wav')
sndEngine = pg.mixer.Sound('sounds/engine.wav')
sndEngine.set_volume(0.5)
sndMove = pg.mixer.Sound('sounds/move.wav')
sndMove.set_volume(0.5)





