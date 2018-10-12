from Adafruit_IO import Client
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
aio = Client('Sundaresan','826788acf84f4e8e86a60916a08ec94e')

while True:
        data = aio.receive('led')
        if data.value == "1" :
                GPIO.output(11,True)
        else:
                GPIO.output(11,False)
        print('Received value: {0}'.format(data.value))


