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

gpio.setup(18,gpio.OUT) 
gpio.setup(37,gpio.OUT)
gpio.setup(29,gpio.OUT)
gpio.setup(31,gpio.OUT)

pasos = [[0,0,1,0],[1,0,1,0], [1,0,0,0],[1,0,0,1],[0,0,0,1],[0,1,0,1],[0,1,0,0],[0,1,1,0]]
pines = [18,37,29,31]


trans = [13,15,16]
pin = [3,5,7,8,10,12,11]

n = [[0,1,1,1,1,1,1],[0,0,0,0,1,1,0],[1,0,1,1,0,1,1],[1,0,0,1,1,1,1],[1,1,0,0,1,1,0],[1,1,0,1,1,0,1],[1,1,1,1,1,0,1]
,[0,0,0,0,1,1,1],[1,1,1,1,1,1,1], [1,1,0,1,1,1,1]]

for i in pin:
    gpio.output(i,0)

while True:
    ################
    gpio.output(trans[0],1)
    gpio.output(trans[1],0)
    gpio.output(trans[2],0)
            
    for i in range(7):
                
        gpio.output(pin[i],1-n[0][i])
        
    x = int(input("Pasos: "))
    
    dig1 = x%10
    dig2 = (x//10)%10
    dig3 = (x//100)%10
    
    inicio = time.time()
        
    while (time.time() - inicio <=3):
            
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

        
###########  

    for num in range(x+1):
        
        dig1 = num%10
        dig2 = (num//10)%10
        dig3 = (num//100)%10
        
        inicio = time.time()
        
        while (time.time() - inicio < 0.03):
            
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
            
        for j in range (4):
             gpio.output(pines[j],pasos[num%8][j])
            
            ##########
        
    dig1 = x%10
    dig2 = (x//10)%10
    dig3 = (x//100)%10
    
    inicio = time.time()
        
    while (time.time() - inicio <=5):
            
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
            ##############################
        
    
