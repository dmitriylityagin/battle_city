from ursina import *
import random
import math

app = Ursina()

camera.orthographic = True
camera.fov = 25

npcs = []
for i in range(12):
    if i < 6:
        rot = 180
        val = -1
    else:
        rot = 0
        val = 1
    npc = Entity(model='cube', texture='assets/npc.png', rotation=rot,
                 position=(random.randint(-15, 10), random.randint(-15, 10)), collider='box', tag='npc')
    npcs.append((npc, val))



Entity(
    model='quad',
    texture="assets/street.png",
    scale=25,
    z=1,
)

player = Entity()
anim = Animator(animations={'idle': Entity(parent=player, model='cube', texture='player.png')})

for i in [-10, 10]:
    for j in [-8, 8]:
        Sprite(model='cube', texture='assets/house.png', scale=3, collider='box', position=(i, j, 0),
               rotation_z=0 if i==4 else 180, tag='house')





# def update():
#     car.x -= held_keys['a'] * 5 * time.dt
#     car.x += held_keys['d'] * 5 * time.dt


# здесь будет описана игровая логика

app.run()
