import pgzrun
import random
WIDTH=700
HEIGHT=400

x1=random.randint(100,600)
y1=random.randint(100,350)
x2=random.randint(100,600)
y2=random.randint(100,350)
x3=random.randint(100,600)
y3=random.randint(100,350)
x4=random.randint(100,600)
y4=random.randint(100,350)
x5=random.randint(100,600)
y5=random.randint(100,350)
x6=random.randint(100,600)
y6=random.randint(100,350)
x7=random.randint(100,600)
y7=random.randint(100,350)
x8=random.randint(100,600)
y8=random.randint(100,350)
x9=random.randint(100,600)
y9=random.randint(100,350)
x10=random.randint(100,600)
y10=random.randint(100,350)

shape1 = Actor("circle")
shape1.pos = ( x1,y1 )
shape2 = Actor("cylinder")
shape2.pos = ( x2,y2 )
shape3 = Actor("decagon")
shape3.pos = ( x3,y3 )
shape4 = Actor("heart")
shape4.pos = ( x4,y4 )
shape5 = Actor("hexagon")
shape5.pos = ( x5,y5 )
shape6 = Actor("parallelogram")
shape6.pos = ( x6,y6)
shape7 = Actor("pentagon")
shape7.pos = ( x7,y7 )
shape8 = Actor("square")
shape8.pos = ( x8,y8 )
shape9 = Actor("trapezium")
shape9.pos = ( x9,y9)
shape10 = Actor("triangle")
shape10.pos = (x10,y10)

numshapes=10
nextshape=0
shapes=[shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9,shape10]
lines=[]

def on_mouse_down(pos):
    global nextshape, lines
    if nextshape < numshapes:
        if shapes[nextshape].collidepoint(pos):
            if nextshape:
                lines.append((shapes[nextshape-1].pos,shapes[nextshape].pos))
            nextshape += 1
        else:
            nextshape = 0
            lines = []

def draw():
    screen.clear()
    shape1.draw()
    screen.draw.text("1",(x1,y1+30))
    shape2.draw()
    screen.draw.text("2",(x2,y2+30))
    shape3.draw()
    screen.draw.text("3",(x3,y3+30))
    shape4.draw()
    screen.draw.text("4",(x4,y4+30))
    shape5.draw()
    screen.draw.text("5",(x5,y5+30))
    shape6.draw()
    screen.draw.text("6",(x6,y6+30))
    shape7.draw()
    screen.draw.text("7",(x7,y7+30))
    shape8.draw()
    screen.draw.text("8",(x8,y8+30))
    shape9.draw()
    screen.draw.text("9",(x9,y9+30))
    shape10.draw()
    screen.draw.text("10",(x10,y10+30))
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
pgzrun.go()