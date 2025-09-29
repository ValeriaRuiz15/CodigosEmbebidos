import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

#Pines 
a1 = 3
a2 = 8
r1 = 5
r2 = 10
v1 = 7
v2 = 12

pv1 = 35
pr1 = 37
pv2 = 36
pr2 = 38

boton = 13

gpio.setup(v1,gpio.OUT) #verde1
gpio.setup(a1,gpio.OUT) #amarillo1
gpio.setup(r1,gpio.OUT) #rojo1

gpio.setup(v2,gpio.OUT) #verde2
gpio.setup(a2,gpio.OUT) #amarillo2
gpio.setup(r2,gpio.OUT) #rojo2

gpio.setup(pv1,gpio.OUT) #pv1
gpio.setup(pr1,gpio.OUT) #pr1

gpio.setup(pv2,gpio.OUT) #pv2
gpio.setup(pr2,gpio.OUT) #pr2

gpio.setup(boton,gpio.IN) #boton

#Todo apagado
gpio.output(a1,0)
gpio.output(v1,0)
gpio.output(r1,0)

gpio.output(a2,0)
gpio.output(v2,0)
gpio.output(r2,0)

gpio.output(pv1,0)
gpio.output(pr1,0)

gpio.output(pv2,0)
gpio.output(pr2,0)

#Peatonal
estado = 0

def peatonal():
    #rojos autos
    gpio.output(a1,0)
    gpio.output(v1,0)
    gpio.output(r1,1)

    gpio.output(a2,0)
    gpio.output(v2,0)
    gpio.output(r2,1)

    #verdes peatonal
    gpio.output(pv1,1)
    gpio.output(pr1,0)

    gpio.output(pv2,1)
    gpio.output(pr2,0)
    time.sleep(5)

    #estado=0 

    #apaga autos
    gpio.output(a1,0)
    gpio.output(v1,0)
    gpio.output(r1,0)

    gpio.output(a2,0)
    gpio.output(v2,0)
    gpio.output(r2,0)

    #rojo peatonal
    gpio.output(pv1,0)
    gpio.output(pr1,1)

    gpio.output(pv2,0)
    gpio.output(pr2,1)



while True:
    #Apaga todos
    gpio.output(a1,0)
    gpio.output(v1,0)
    gpio.output(r1,0)

    gpio.output(a2,0)
    gpio.output(v2,0)
    gpio.output(r2,0)

    gpio.output(pv1,0)
    gpio.output(pr1,0)

    #rojo peatonal
    gpio.output(pr1,1)
    gpio.output(pr2,1)

    t1 = time.time()

    while(time.time()-t1 <= 5):
        gpio.output(v1,1) # verde sem1
        gpio.output(r2,1) #rojo sem2

        if(gpio.input(boton)): #si presiona cambia 
            estado=1

    #parpadeo de verde autos
    for i in range(3):
        gpio.output(v1,1)
        time.sleep(0.3)
        gpio.output(v1,0)
        time.sleep(0.3)


    t1 = time.time()

    if (estado==1): #peatonal
        peatonal()
        estado = 0 


    while(time.time()-t1 <= 3):
        gpio.output(a1,1) #amarillo sem1
        if(gpio.input(boton)): #cambio de estado
            estado=1

    gpio.output(a1,0) 

    t1 = time.time()
    while(time.time()-t1 <= 5):
        gpio.output(v2,1)
        gpio.output(r1,1)

        if(gpio.input(boton)):
            estado=1


    for i in range(3):
        gpio.output(v2,1)
        time.sleep(0.3)
        gpio.output(v2,0)
        time.sleep(0.3)

    if (estado==1):
        peatonal()
        estado=0


    t1 = time.time()
    while(time.time()-t1 <= 3):
        gpio.output(a2,1)
        if(gpio.input(boton)):
            estado=1




