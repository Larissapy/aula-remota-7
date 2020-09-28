from turtle import *

def draw_planet(planetsize, planetcolour):
    color(planetcolour)
    pendown()
    begin_fill()

    circle(planetsize)

    end_fill()
    penup()



bgcolor('midnightblue')

draw_planet(60, '#D2691E')
forward(200)
draw_planet(40, '#1E90FF')
right(150)
forward(200)
draw_planet(90, '#ADFF2F')

hideturtle()
done()