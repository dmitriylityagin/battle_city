# Создание, отрисовка и управление танками
import pygame
from random import *
from class_tank import Tank
from framedraw import window, FPS, TILE, WIDTH, HEIGHT, imgBonuses, sndMove, sndEngine, bonusTimer, timer, isMove, isWin
from game_object import objects
from class_bullets import bullets
from class_block import Block
from class_ui import UI
from class_bonus import Bonus

pygame.init()

clock = pygame.time.Clock()

player = Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q))
player2 = Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_e))

pygame.mixer.music.load('sounds/level_start.mp3')
pygame.mixer.music.play()

ui = UI()


for _ in range(50):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(0, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect): fined = True

        if not fined: break

    Block(x, y, TILE)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    timer += 1
    if timer >= 260 and not isWin:
        if oldIsMove != isMove:
            if isMove:
                sndMove.play()
                sndEngine.stop()

            else:
                sndMove.stop()
                sndEngine.play(-1)

    oldIsMove = isMove
    isMove = False
    for obj in objects:
        if obj.type == 'tank': isMove = isMove or obj.isMove

    if bonusTimer > 0:
        bonusTimer -= 1
    else:
        Bonus(randint(50, WIDTH - 50), randint(50, HEIGHT - 50), randint(0, len(imgBonuses) - 1))
        bonusTimer = randint(120, 240)

    for bullet in bullets:
        bullet.update()
    for obj in objects:
        obj.update()

    ui.update()

    window.fill('black')

    for bullet in bullets:
        bullet.draw()
    for obj in objects:
        obj.draw()

    ui.draw()

    if isWin and timer == 1000:
        sndMove.stop()
        sndEngine.stop()

        pygame.mixer.music.load('sounds/level_finish.mp3')
        pygame.mixer.music.play()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

