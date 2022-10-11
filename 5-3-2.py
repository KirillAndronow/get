from signal import signal
import RPi.GPIO as GPIO
import time

def binary(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
j=0
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
level = 256
comp = 4
troyka = 17
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def numDAC(value):
    signal = binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    value = 0
    for i in range(dac):
        GPIO.output(dac(-i+7), 1)
        compValue = GPIO.input(comp)
        if compValue == 1:
            GPIO.output(dac(-i+7), 0)
        elif compValue == 0:
            value += 2**(-i+7)
        time.sleep(0.0007)
    return value


try:
    while True:
        ADC = adc()
        V = ADC/level * 3.3
        if j*3.3/8 < ADC <= (j+1)*3.3/8:
            if j*3.3/8 > ADC:
                GPIO.output(leds[i], 0)
                j-=j
        else:
            GPIO.output(leds[i], 1)
            j+=j
        print("ADC value = {:^3}, {}, Voltage = {:.2f}".format(ADC,binary(ADC),V))

except KeyboardInterrupt:
    print('\nПрограмма была остановлена с клавиатуры')

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()