from pickle import TRUE
from signal import signal
import RPi.GPIO as GPIO
import time

def binary(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
level = 256
comp = 4
troyka = 17
i=0
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def numDAC(value):
    signal = binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    for value in range(level):
        signaL = numDAC(value)
        time.sleep(0.0007)
        V = value/level * 3.3
        compValue = GPIO.input(comp) 
        if compValue == 0:
            print("ADC value = {:^3} -> {}, Voltage = {:.2f}".format(value, signaL, V))
            break
    return value

try:
    while True:
        ADC = adc()
        V = ADC/level * 3.3
        if i*3.3/8 < ADC <= (i+1)*3.3/8:
            if i*3.3/8 > ADC:
                GPIO.output(leds[i], 0)
                i-=i
        else:
            GPIO.output(leds[i], 1)
            i+=i
        print("ADC value = {:^3}, Voltage = {:.2f}".format(ADC, V))

except KeyboardInterrupt:
    print('\nПрограмма была остановлена с клавиатуры')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()
