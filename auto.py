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
bricks = go.Bricks()


def auto_down():
    while True:
        time.sleep(cfg.TIME_SLEEP)
        global bricks, field, window
        bricks.control_brick(ord("s"), field)
        can_down = utils.check_valid(field, bricks)
        if not can_down:
            bricks.revert()
            field.add_bricks(bricks)
            bricks = go.Bricks()
            field.check_and_clear_rows()
        # render screen
        rendered = utils.create_screen(field, bricks)
        window.refresh()
        window.addstr(0, 0, rendered)


def move(key):
    global bricks, field, window
    window.clear()
    window.refresh()
    bricks.control_brick(key, field)

    # check valid move or not
    valid = utils.check_valid(field, bricks)
    if not valid:
        bricks.revert()

    # check_get floor
    bricks.control_brick(ord("s"), field)
    can_down = utils.check_valid(field, bricks)
    bricks.revert()
    if not can_down:
        field.add_bricks(bricks)
        bricks = go.Bricks()

    # clear one row when full
    field.check_and_clear_rows()

    # render screen
    rendered = utils.create_screen(field, bricks)
    window.addstr(0, 0, rendered)


def move_set(keys_list):
    global window
    move(keys_list[0])
    for key in keys_list[1:]:
        window.getch()
        move(key)


Thread(target=auto_down).start()

while True:
    window.getch()
    keys_list = utils.get_moveset(field, bricks)
    move_set(keys_list)
