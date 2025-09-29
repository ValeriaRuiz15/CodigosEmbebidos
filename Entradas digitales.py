import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.IN)
gpio.setup(8,gpio.OUT)

while True:
    try:
        if gpio.input(7) == True:
            gpio.output(8,1)
        else:
            gpio.output(8,0)
        time.sleep(0.01)
        
    except KeyboardInterrupt:
        print("Programa terminado")
        gpio.output(8,0)
        raise