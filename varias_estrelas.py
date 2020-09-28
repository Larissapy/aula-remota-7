from turtle import *
from random import *


def move_to_random_location():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()


def draw_star(star_size, star_colour):
    color(star_colour)
    pendown()
    begin_fill()

    for side in range(5):
        left(144)
        forward(star_size)

    end_fill()
    penup()

bgcolor('midnightblue')

for star in range(30):
    move_to_random_location()
    draw_star(randint(5, 25), 'white')

hideturtle()
done()