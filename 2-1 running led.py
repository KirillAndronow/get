import RPi.GPIO as GPIO
import time
counter = 0
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

while counter < 3:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
        counter +=1


GPIO.output(leds, 0)
GPIO.cleanup()