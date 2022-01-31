import sys
import time
import RPi.GPIO as io
import subprocess
from datetime import datetime




io.setmode(io.BCM)
SHUTOFF_DELAY = 120 # seconds
PIR_PIN = 4       # 22 on the board
LED_PIN = 16

def main():
    io.setup(PIR_PIN, io.IN)
    io.setup(LED_PIN, io.OUT)
    turned_off = False
    last_motion_time = time.time()

    while True:
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            io.output(LED_PIN, io.LOW)
       	    now = datetime.now().time() # time object
            print now
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + 
                                                 SHUTOFF_DELAY):
                turned_off = True
                turn_off()
            if not turned_off and time.time() > (last_motion_time + 1):
                io.output(LED_PIN, io.HIGH)
        time.sleep(.1)

def turn_on():
    subprocess.call("sh /home/pi/monitor_on.sh", shell=True)

def turn_off():
    subprocess.call("sh /home/pi/monitor_off.sh", shell=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
