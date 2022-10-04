import RPi.GPIO as GPIO
import time

def binary(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(x, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
# p = GPIO.PWM(x, 0.5)

try:
    while True:
        D = input('Введите коэффициент заполнения, в процентах:')
        f = input('Введите частоту в Гц:')
        p = GPIO.PWM(x, 0.5)
        p.start(D)
        print('Текущее напряжение на выходе ЦАП примерно равно:', 3.3 * D * 0.01)
        p.stop()
        

finally:
    GPIO.output(x, 0)
    GPIO.cleanup()