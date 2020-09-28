from turtle import *

def square():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(50)
    end_fill()
    penup()

def triangle():
    pendown()
    begin_fill()
    for c in range(3):
        forward(50)
        left(120)
    end_fill()
    penup()

def circle():
    pendown()
    begin_fill()
    for cout in range(360):
        forward(1)
        right(1)
    end_fill()
    penup()


color('whitesmoke')
bgcolor('navy')

square()
forward(100)
triangle()
left(90)
forward(150)
circle()
right(90)
forward(100)

hideturtle()
done()



