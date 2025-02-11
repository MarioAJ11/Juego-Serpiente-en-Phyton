# CONTROLAMOS LA ENTRADA POR TECLADO
import tkinter.messagebox
import turtle
import time
import random
import os

# Esta variable dependerá de cada equipo
retrasar = 0.1

puntuacion = 0
def obtener_max_puntuacion():
    try:
        with open("max_puntuacion.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def guardar_max_puntuacion():
    with open("max_puntuacion.txt", "w") as f:
        f.write(str(puntuacion))

maxPuntuacion = obtener_max_puntuacion()
vida = 3
# Configurar la ventana
ventana = turtle.Screen()
ventana.title("Juego de SNAKE")
ventana.bgcolor("green")
# Determinamos el tamaño de la ventana
ventana.setup(width=600,height=600)
ventana.resizable(False, False)
# Hace más visual la animación
ventana.tracer(0)

# Dibujar la cabeza de la serpiente con turtle.Turtle() lo que conseguimos es una pluma
cabeza = turtle.Turtle()
# Cuando arranque el juego lo que queremos es que esté quieta la pluma/serpiente
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("blue")
# Quitamos el rastro de movimiento de la pluma
cabeza.penup()
# No funciona como en Java, sino que tenemos eje x e y, el centro es 0,0 y arriba izq sería -50, -50 (por ejemplo)
cabeza.goto(0,0)
# Indicamos la direccion de la pluma
cabeza.direction = "stop"

def posicionComida():
    #al principio en una coordenadas aleatorias
    x = 0
    y = 0
    #Debemos asegurarnos de que no se ha generado 0,0
    while x == 0 and y == 0:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
    comida.goto(x,y)

def posicionBomba():
    x = 0
    y = 0
    while x == 0 and y == 0:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        while comida.distance(x,y) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 260) 
    bomba.goto(x,y)
#CUERPO
segmentos = []

#MARCADOR
marcador = turtle. Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()#no aparece la pluma
marcador.hideturtle()
marcador.goto(0,270)
marcador.write(f"Puntuación: {puntuacion}     Max. puntuacion: {maxPuntuacion}      VIDA: {vida}", align="center", font="Courier")

#LÍNEA MARCADOR
linea = turtle. Turtle()
linea.speed(0)
linea. shape("square")
linea.color("white")
linea.penup()
linea.shapesize(stretch_wid=0.1,stretch_len=30)#Ancho muy delgado, longitud toda la ventana
linea.goto(0, 270)  

#COMIDA PLUS
comidaPlus = turtle.Turtle()
comidaPlus.speed(0)
comidaPlus.shape("circle")
comidaPlus.color("pink")
comidaPlus.penup()
comidaPlus.hideturtle()

#COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
posicionComida()

#BOMBA
bomba = turtle.Turtle()
bomba.speed(0)
bomba.shape("turtle")
bomba.color("black")
bomba.penup()
posicionBomba()

# Declaramos las funciones de dirección antes porque el lenguaje lo requiere
def arriba():
    # Indicamos la direccion de la pluma
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

# ESCUCHAR EL TECLADO DESDE LA VENTANA
ventana.listen()
ventana.onkeypress(arriba, "Up") # Podríamos usar "w" y al pulsarlo, llamamos a la función SIN PARENTESIS
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Vamos a definir las funciones de movimiento
def mov():
    if cabeza.direction == "up":
        # Pedimos las coordenada y
        y = cabeza.ycor()
        # Actualizamos la coordenada y con 20 pixeles más (el ancho de la cabeza)
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        # Pedimos las coordenada y
        y = cabeza.ycor()
        # Actualizamos la coordenada y con 20 pixeles más (el ancho de la cabeza)
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        # Pedimos las coordenada x
        x = cabeza.xcor()
        # Actualizamos la coordenada x con 20 pixeles más (el ancho de la cabeza)
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        # Pedimos las coordenada x
        x = cabeza.xcor()
        # Actualizamos la coordenada x con 20 pixeles más (el ancho de la cabeza)
        cabeza.setx(x + 20)

def limpiarSegmentos():
    for segmento in segmentos:
        segmento.hideturtle()
        segmento.clear()
    segmentos.clear()
    cabeza.goto(0,0)
    posicionComida()
    posicionBomba()
    cabeza.direction = "stop"
    puntuacion = 0
    maxPuntuacion = obtener_max_puntuacion()
    marcador.clear()
    marcador.write(f"Puntuación: {puntuacion}     Max. puntuacion: {maxPuntuacion}      Vida: {vida}", align="center", font="Courier")
    print("Has perdido tus vidas se reiniciara todo el cuerpo")

def reiniciarCuerpo():
    cabeza.goto(0,0)
    for segmento in segmentos:
        segmento.goto(400,400)
    posicionComida()
    posicionBomba()
    cabeza.direction = "stop"
    marcador.clear()
    marcador.write(f"Puntuación: {puntuacion}     Max. puntuacion: {maxPuntuacion}      Vida: {vida}", align="center", font="Courier")
    print("Has perdido tus vidas se reiniciara al centro")


print("Bienvenido snake pro, que disfrute el juego.")
try:  
    while puntuacion <= 1000:
        # Actualizamos la ventana continuamente, para que muestre los cambios
        ventana.update()
        if cabeza.distance(comida) < 20:
            comidaPlus.hideturtle()
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("lightblue")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)

            if(cabeza.distance(comidaPlus) < 20):
                nuevo_segmento2 = turtle.Turtle()
                nuevo_segmento2.speed(0)
                nuevo_segmento2.shape("square")
                nuevo_segmento2.color("pink")
                nuevo_segmento2.penup()
                segmentos.append(nuevo_segmento2)
                puntuacion += 10

            puntuacion += 10
            maxPuntuacion = obtener_max_puntuacion()
            marcador.clear()
            marcador.write(f"Puntuación: {puntuacion}     Max. puntuacion: {maxPuntuacion}      Vida: {vida}", align="center", font="Courier")
            if puntuacion > maxPuntuacion:
                guardar_max_puntuacion()
            r = random.randint(1, 10)
            while True:
                x = random.randint(-280, 280)
                y = random.randint(-280, 260)
                disponible = True
                for segmento in segmentos:
                    if segmento.distance(x, y) < 20:
                        disponible = False
                if disponible:  
                    if r == 1:
                        comida.goto(x, y)
                        comida.hideturtle()
                        comidaPlus.goto(x, y)
                        comidaPlus.showturtle()
                    else:
                        comida.goto(x, y)
                        comida.showturtle()
                    break       
                    
        if cabeza.distance(bomba) < 20:
            vida-=1
            if vida == 0:
                vida = 3
                limpiarSegmentos()
            else:
                reiniciarCuerpo()
                

        if cabeza.direction != "stop":
            totalSegmentos = len(segmentos)
            for i in range(totalSegmentos - 1, 0, -1):
                x = segmentos[i - 1].xcor()
                y = segmentos[i - 1].ycor()
                segmentos[i].goto(x, y)

            if totalSegmentos > 0:
                x = cabeza.xcor()
                y = cabeza.ycor()
                segmentos[0].goto(x, y)

        if cabeza.xcor() == 300 or cabeza.xcor() == -300 or cabeza.ycor() == 260 or cabeza.ycor() == -300:
            vida-=1
            if vida == 0:
                vida = 3
                limpiarSegmentos()
            else:
                reiniciarCuerpo()
            
            
        
        mov()

        for segmento in segmentos:
            if segmento.distance(cabeza) < 20:
                vida-=1
                if vida == 0:
                    vida = 3
                    limpiarSegmentos()
                else:
                    reiniciarCuerpo()     
            
        time.sleep(retrasar)
    
    print("wow, que locura")
    tkinter.messagebox.showinfo("no me jodas", "En serio te gastas el tiempo de tu vida en esto, ya me jodería :)\n MANDA CAPTURA DE ESTE MENSAJE AL CREADOR") 
    turtle.Screen()._root.protocol("WM_DELETE_WINDOW")
except turtle.Terminator:
    print("A chuparla ya de aquí")
