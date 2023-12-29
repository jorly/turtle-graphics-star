"""
Author: Jorly Metzger ,metzge30@purdue.edu
License: GPLv3
Date: 10/09/2023

Description:
    Uses Turtle graphics to draw a star
"""

"""Import modules"""
from turtle import *

"""Classes and Functions"""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

""" === MAIN === """

####
# Uses a for loop to draw a star using Turtle graphics.  Number of
# points in the star in determined through user input
# ##
def main():
    points = int(input("Enter number of points for your star: "))
    edges = 0
    inner = 360 / points
    outer = 2 * inner

    start()
    color("black", "yellow")
    begin_fill()
    right (90 - inner)

    while edges < points*2:
        forward (60)
        edges += 1

        if (edges % 2) == 0:
            right (180 - outer)
        else:
            left (180 - inner)
    end_fill()


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
