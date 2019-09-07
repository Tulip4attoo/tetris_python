import curses
import time
import game_objects as go
import utils
from threading import Thread


window = curses.initscr()
curses.cbreak()
curses.noecho()

field = go.Field()
bricks = go.Bricks()


def func1():
    while True:
        time.sleep(1)
        global bricks, field, count
        bricks.control_brick(ord("s"))
        can_down = utils.check_valid(field, bricks)
        if not can_down:
            bricks.revert()
            field.add_bricks(bricks)
            bricks = go.Bricks()
            field.check_and_clear_rows()
        # render screen
        rendered = utils.create_screen(field, bricks)
        # window.clear()
        window.refresh()
        window.addstr(0, 0, rendered)

Thread(target=func1).start()

while True:
    # get key
    key = window.getch()
    window.clear()
    window.refresh()
    bricks.control_brick(key)

    # check valid move or not
    valid = utils.check_valid(field, bricks)
    if not valid:
        bricks.revert()

    # check_get floor
    bricks.control_brick(ord("s"))
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
