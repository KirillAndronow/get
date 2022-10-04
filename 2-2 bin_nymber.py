import RPi.GPIO as GPIO
import time
counter = 0
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 1, 1, 1, 0, 0, 1]

#number = [0, 0, 1, 0]   2
#number = [1, 1, 1, 1, 1, 1, 1, 1]   255
#number = [0, 1, 1, 1, 1, 1, 1, 1]   127
#number = [0, 1, 0, 0, 0, 0, 0, 0]   64
#number = [0, 0, 1, 0, 0, 0, 0, 0]   32
#number = [0, 1, 0, 1]   5
#number = [0, 0, 0, 0, 0, 0, 0, 0]   0
#number = [0, 0, 0, 0]   256



GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in dac and number:
    GPIO.output(i, i)
    
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()

