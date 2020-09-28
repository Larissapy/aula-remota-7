from turtle import *

def draw_star(starsize, starcolour):
    color(starcolour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starsize)
    end_fill()
    penup()



bgcolor('midnightblue')

draw_star(50, '#EE82EE')
forward(100)
draw_star(30, '#B0E0E6')
left(120)
forward(150)
draw_star(70, '#00FFFF')

hideturtle()
done()