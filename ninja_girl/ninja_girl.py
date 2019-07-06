from time import sleep
from enum import Enum
import pgzrun

ninja_girl = Actor('ninja-girl/idle/idle__000')
ninja_girl.pos = 200, 200
WIDTH = 1800
HEIGHT = 500

idle_number = 0
run_number = 0
is_running = False


def draw():
    screen.clear()
    x, y = ninja_girl.pos
    screen.draw.text(f'X:{x},Y:{y}', (20, 20))
    ninja_girl.draw()


class Facing(Enum):
    RIGHT = 1
    LEFT= 2

def update():
    if keyboard.right:
        is_running = True
        facing = Facing.RIGHT
    elif keyboard.left:
        is_running = True
        facing = Facing.LEFT
    else:
        is_running = False
        facing_right = False
        facing_left = False

    if is_running and facing == Facing.RIGHT:
        x, y = ninja_girl.pos
        x = x + 20
        if x > WIDTH:
            x = 0
        ninja_girl.pos = x, y
        play_run()
    elif is_running and facing == Facing.LEFT:
        x, y = ninja_girl.pos
        x = x - 20
        if x > WIDTH:
            x = 0
        ninja_girl.pos = x, y
        play_run()
    else:
        play_idle()


def play_idle():
    global idle_number
    idle_number = idle_number + 1
    sleep(0.1)
    if idle_number > 9:
        idle_number = 0
    ninja_girl.image = f'ninja-girl/idle/idle__00{idle_number}'


def play_run():
    global run_number
    run_number = run_number + 1
    sleep(0.1)
    if run_number > 9:
        run_number = 0
    ninja_girl.image = f'ninja-girl/run/run__00{run_number}'


pgzrun.go()
