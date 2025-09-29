import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

gpio.setup(3,gpio.OUT) 
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(10,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(11,gpio.OUT)

gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(16,gpio.OUT)


trans = [13,15,16]
pin = [3,5,7,8,10,12,11]

n = [[0,1,1,1,1,1,1],[0,0,0,0,1,1,0],[1,0,1,1,0,1,1],[1,0,0,1,1,1,1],[1,1,0,0,1,1,0],[1,1,0,1,1,0,1],[1,1,1,1,1,0,1]
,[0,0,0,0,1,1,1],[1,1,1,1,1,1,1], [1,1,0,1,1,1,1]]

for i in pin:
    gpio.output(i,0)

while True:
    
    for num in range(1000):
        
        dig1 = num%10
        dig2 = (num//10)%10
        dig3 = (num//100)%10
        
        inicio = time.time()
        
        while (time.time() - inicio < 1):
            
            gpio.output(trans[0],1)
            gpio.output(trans[1],0)
            gpio.output(trans[2],0)
            
            for i in range(7):
                
                gpio.output(pin[i],1-n[dig1][i])
                
            time.sleep(0.006)
                
                
            gpio.output(trans[0],0)
            gpio.output(trans[1],1)
            gpio.output(trans[2],0)
            
            for i in range(7):
                
                gpio.output(pin[i],1-n[dig2][i])
                
            time.sleep(0.006)
                
            gpio.output(trans[0],0)
            gpio.output(trans[1],0)
            gpio.output(trans[2],1)
            
            for i in range(7):
                
                gpio.output(pin[i],1-n[dig3][i])
            
            time.sleep(0.006)
                            
                
            
     










