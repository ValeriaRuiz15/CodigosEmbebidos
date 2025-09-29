import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)

print("Inicindo")

gpio.output(3,0)

for i in range(0,5):
    gpio.output(3,1)
    time.sleep(1)
    gpio.output(3,0)
    time.sleep(1)


gpio.output(3,0)

print("terminado")

gpio.cleanup()