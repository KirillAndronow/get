import RPi.GPIO as GPIO
import time
counter = 0
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
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
GPIO.setup(aux, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

for i in leds:
    GPIO.output(i, 1)

while True:
    for i in leds and:
        for j in aux :
        GPIO.output(i, GPIO.output(j, 0))
    


GPIO.output(leds, 0)
GPIO.cleanup()