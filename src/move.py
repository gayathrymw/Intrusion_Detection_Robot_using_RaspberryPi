#!/usr/bin/python3.7
from gpiozero import Motor
import curses

blmotor = Motor(forward=9, backward=11)
brmotor = Motor(forward=10, backward=12)

def left():
    print('Left ...')
    brmotor.forward()

def right():
    print('Right ...')
    blmotor.forward()

def forward():
    print('Forwarding ...')
    blmotor.forward()
    brmotor.forward()

def reverse():
    print('Reversing ...')
    blmotor.backward()
    brmotor.backward()

def stop():
    print('Stopping ...')
    blmotor.stop()
    brmotor.stop()

actions = {
    curses.KEY_UP:    forward,
    curses.KEY_DOWN:  reverse,
    curses.KEY_LEFT:  left,
    curses.KEY_RIGHT: right,
}

def main(window):

    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            stop()


if __name__ == "__main__":
    curses.wrapper(main)
