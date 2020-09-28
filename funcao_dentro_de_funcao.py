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

def draw_galaxy(number_of_stars):
    stars_colours = ['#058396', '#0275A6', '#827E01']
    move_to_random_location()

    for star in range(number_of_stars):
        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()

        draw_star(2, choice(stars_colours))

def draw_constellation(number_of_stars):
    move_to_random_location()

    for star in range(number_of_stars - 1):
        draw_star(randint(7, 15), 'white')
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))

    draw_star(randint(7, 15), 'white')

speed(11)
bgcolor('midnightblue')

for star in range(30):
    move_to_random_location()
    draw_star(randint(5, 25), 'white')

for galaxy in range(3):
    draw_galaxy(40)

for constellation in range(2):
    draw_constellation(randint(4, 7))

hideturtle()
done()
