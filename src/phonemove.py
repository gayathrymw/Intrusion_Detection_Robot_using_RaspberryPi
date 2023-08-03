from flask import Flask, render_template, request
from gpiozero import Motor
import curses
import threading
import time

app = Flask(__name__)

blmotor = Motor(forward=9, backward=11)
brmotor = Motor(forward=10, backward=12)

def left():
    brmotor.forward()

def right():
    blmotor.forward()

def forward():
    blmotor.forward()
    brmotor.forward()

def reverse():
    blmotor.backward()
    brmotor.backward()

def stop():
    blmotor.stop()
    brmotor.stop()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

'''
@app.route('/control', methods=['POST'])
def control():
    key = int(request.json['key'])
    action = actions.get(key)
    if action is not None:
        action()
        # Stop the robot after 1 second (adjust as needed)
        time.sleep(1)
        stop()
    return '', 204  # Return a success response without content
    '''
@app.route('/control', methods=['POST'])
def control(): # server receives the control inputs
    key = request.form['direction']  
    if key == 'forward':  
        forward()
    elif key == 'reverse':  
        reverse()
    elif key == 'left':  
        left()
    elif key == 'right':  
        right()
    elif key == 'stop':  
        stop()

    return '', 204
    
    '''
actions = {
    curses.KEY_UP:    forward,
    curses.KEY_DOWN:  reverse,
    curses.KEY_LEFT:  left,
    curses.KEY_RIGHT: right,
}

def main():
    curses.wrapper(curses_main)

def curses_main(window):
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
    '''

if __name__ == "__main__":
    '''
    Start the web server in a separate thread
    web_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5005})
    web_thread.daemon = True
    web_thread.start()

    # Start the main robot control function
    #main()
    '''
    app.run(host='0.0.0.0', port=5005)
