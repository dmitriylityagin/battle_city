# Создание, отрисовка и управление танками
import pygame
from class_tank import Tank,objects
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32
clock = pygame.time.Clock()

player = Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_QUESTION))
player2 = Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_q))
window = player.window
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    
    for obj in objects: obj.update()

    window.fill('black')
    for obj in objects: obj.draw()
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
