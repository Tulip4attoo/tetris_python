import main
import curses

window = curses.initscr()
curses.noecho()
window.keypad(True)  # Maybe not perfect, but a good start?

while True:
    event = window.getch()
    default_key = "string ne"
    key = default_key if event == -1 else event
    print(f'k: {key}')
    # curses.flushinp()
