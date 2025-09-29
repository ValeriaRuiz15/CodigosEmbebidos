import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

gpio.setup(18,gpio.OUT) 
gpio.setup(37,gpio.OUT)
gpio.setup(29,gpio.OUT)
gpio.setup(31,gpio.OUT)


#pasos = [[1,1,0,0], [0,1,1,0],[0,0,1,1],[1,0,0,1]]
pasos = [[0,0,1,0],[1,0,1,0], [1,0,0,0],[1,0,0,1],[0,0,0,1],[0,1,0,1],[0,1,0,0],[0,1,1,0]]
pines = [18,37,29,31]

while True:
    
    for i in range(8):
        for j in range (4):
             gpio.output(pines[j],pasos[i][j])
             
        time.sleep(0.001)

