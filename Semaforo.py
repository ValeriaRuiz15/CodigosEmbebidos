import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT) #verde
gpio.setup(5,gpio.OUT) #amarillo
gpio.setup(7,gpio.OUT) #rojo

print("Inicindo")

gpio.output(3,0)
gpio.output(5,0)
gpio.output(7,0)

while True:
    gpio.output(3,1)
    time.sleep(4)
    gpio.output(3,0)
    
    for i in range(3):
        gpio.output(3,1)
        time.sleep(0.5
                   )
        gpio.output(3,0)
        time.sleep(0.5)
    
    gpio.output(5,1)
    time.sleep(2)
    gpio.output(5,0)
    gpio.output(5,0)
    gpio.output(7,1)
    time.sleep(4)
    gpio.output(7,0)
    
    
        
    
    