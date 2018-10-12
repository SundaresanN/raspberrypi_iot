import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)
from Adafruit_IO import Client
aio = Client('826788acf84f4e8e86a60916a08ec94e')
switch = aio.feeds('switch')
while True:
        input_state=GPIO.input(11)
        if input_state == False:
           aio.send_data(switch.key , 'ON')
           print('Button Pressed')
        else:
           aio.send_data(switch.key , 'OFF')
           print('Button not pressed')
