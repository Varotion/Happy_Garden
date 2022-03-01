from tkinter import W
from turtle import color
from weakref import finalize
import pgzrun
import time
import random

WIDTH  =800
HEIGHT = 600

flower_list = []
wilted_list = []
garden_happy = True
game__over = False
fangflower_list = []
time_elapsed = 0
fangflower_vx_list = []
fangflower_vy_list = []



start_game = time.time()

cow = Actor('cow', (100,500))

def draw():
    global game__over, time_elapsed,finalized,fangflower_list
    if not game__over:
        screen.clear()
        time_elapsed = int (time.time() - start_game)
        screen.blit('garden', (0,0))
        screen.draw.text(
                    text=f'garden happy for {time_elapsed } seccond',
                    topleft = (20,20),
                    color='green'
                    )
    cow.draw()
    for flower in flower_list:
        flower.draw()
    for fangflower in fangflower_list:
        fangflower.draw()   
    else:
        if not garden_happy:
            screen.draw.text("GARDEN UNHAPPY! GAME OVER!", color="black", topleft=(10,50))
            finalized= True

def update():

    pass


def new_flower():
    global flower_list,wilted_list
    flower = Actor('flower')
    x = random.randint(100, WIDTH - 100)
    y = random.randint(200, HEIGHT -50)
    flower.pos = (x,y)

    flower_list.append(flower)
    wilted_list.append('happy')

def add_flowers():
    global game__over
    if not game__over:
        new_flower()
        clock.schedule(add_flowers, 4)

add_flowers()

def wilt_flower():
    global flower_list, wilted_list,game__over
    if not game__over:
        if flower_list:
            rand_flower = random.randint(0, len(flower_list)-1)
            if flower_list[rand_flower].image == "flower":
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower,3)

wilt_flower()

def check_wilt_times():
    global wilted_list, game__over, garden_happy
    if wilted_list:
        for wilted_since in wilted_list:
            if not wilted_since == "happy":
                time_wilted = int(time.time() - wilted_since)
                if time_wilted > 100:
                    garden_happy = False
                    game__over = True
                    break

def mutate():
    global flower_list, fangflower_list,game__over,fangflower_vx_list,fangflower_vy_list
    if not game__over and flower_list:
        rand_flower = random.randint(0, len(flower_list) -1)
        fang_flower_pos_x = flower_list[rand_flower].x
        fang_flower_pos_y = flower_list[rand_flower].y
        del flower_list[rand_flower]
        fang_flower = Actor("fangflower")
        fang_flower.pos = fang_flower_pos_x, fang_flower_pos_y
        fangflower_vx = velocity()
        fangflower_vy = velocity()
        fangflower_list.append(fang_flower)
        fangflower_vy_list.append(fangflower_vy)
        fangflower_vx_list.append(fangflower_vx)
        clock.schedule(mutate, 20)

def velocity():
    random_dir = random.randint(0,1)
    random_velocity = random.randint(2,3)
    if random_dir == 0:
        return -random_velocity
    else:
        return random_velocity

def update_fangflowers():
    global fangflower_list, game__over
    if not game__over:
        for index, fangflower in enumerate(fangflower_list):
            fangflower_vx = fangflower_vx_list[index]
            fangflower_vy = fangflower_vy_list[index]
            fangflower.x += fangflower_vx
            fangflower.y += fangflower_vy
            if fangflower.left < 0:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.right > WIDTH:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.top < 150:
                fangflower_vy_list[index] = -fangflower_vy
            if fangflower.bottom > HEIGHT:
                fangflower_vy_list[index] = -fangflower_vy

def update():
    global game__over,flower_list,fangflower_list, time_elapsed
    check_wilt_times()
    if not game__over:
        if time_elapsed > 15 and not fangflower_list:
            mutate()
        update_fangflowers()




pgzrun.go()