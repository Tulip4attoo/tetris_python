import curses
import time
import game_objects as go
import utils
from threading import Thread
import cfg


window = curses.initscr()
curses.cbreak()
curses.noecho()
window.timeout(cfg.TIME_MOVE_SET)

field = go.Field()
brick = go.Brick()


def auto_down():
    while True:
        time.sleep(cfg.TIME_SLEEP)
        global brick, field, window
        brick.control_brick(ord("s"), field)
        can_down = utils.check_valid(field, brick)
        if not can_down:
            brick.revert()
            field.add_brick(brick)
            brick = go.brick()
            field.check_and_clear_rows()
        # render screen
        rendered = utils.create_screen(field, brick)
        window.refresh()
        window.addstr(0, 0, rendered)


def move(key):
    global brick, field, window
    window.clear()
    window.refresh()
    brick.control_brick(key, field)

    # check valid move or not
    valid = utils.check_valid(field, brick)
    if not valid:
        brick.revert()

    # check_get floor
    brick.control_brick(ord("s"), field)
    can_down = utils.check_valid(field, brick)
    brick.revert()
    if not can_down:
        field.add_brick(brick)
        brick.create_new_brick()

    # clear one row when full
    field.check_and_clear_rows()

    # render screen
    rendered = utils.create_screen(field, brick)
    window.addstr(0, 0, rendered)


def move_set(keys_list):
    global window
    move(keys_list[0])
    for key in keys_list[1:]:
        window.getch()
        move(key)

# turnoff auto down in auto mode for testing

# Thread(target=auto_down).start()

while True:
    window.getch()
    keys_list = utils.get_moveset(field, brick)
    move_set(keys_list)
