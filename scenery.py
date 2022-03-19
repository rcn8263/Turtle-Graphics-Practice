"""
   Use turtle graphics to draw a forest scene

   assignment: Lab 1
   file: forest_scenery.py
   author: Ryan Nowak
"""

# imports

import turtle as tt
import math
import random

# definitions


def draw_pine_tree(trunk_len):
    """
    draw_pine_tree draws a pine tree of random length at
    turtle's position

    trunk_len -- integer between 50 and 200 pixels

    returns: amount of ink to draw tree in pixels

    pre-condition: tt is at the base of the tree,
                   pen is up, and is facing up

    post-condition: tt is at the base of the tree,
                    pen is up, and is facing up
    """
    tt.color('Green')
    tt.down()
    tt.forward(trunk_len)
    tt.right(90)
    tt.forward((trunk_len * 0.6) / 2)
    tt.left(120)
    tt.forward(trunk_len * 0.6)
    tt.left(120)
    tt.forward(trunk_len * 0.6)
    tt.left(120)
    tt.forward((trunk_len * 0.6) / 2)
    tt.left(90)
    tt.back(trunk_len)
    tt.up()

    return trunk_len + 3 * (trunk_len * 0.6)


def draw_maple_tree(trunk_len):
    """
    draw_maple_tree draws a maple tree of random length at
    turtle's position

    trunk_len -- integer between 50 and 150 pixels

    returns: amount of ink to draw tree in pixels

    pre-condition: tt is at the base of the tree,
                   pen is up, and is facing up

    post-condition: tt is at the base of the tree,
                    pen is up, and is facing up
    """
    tt.color('Green')
    tt.down()
    tt.forward(trunk_len)
    tt.right(90)
    tt.circle(trunk_len * 0.4)
    tt.left(90)
    tt.back(trunk_len)
    tt.up()

    return trunk_len + 2 * math.pi * (trunk_len * 0.4)


def draw_house(color):
    """
    draw_house draws a house at
    turtle's position

    color -- string, specifies color of ink for house

    returns: amount of ink to draw house in pixels

    pre-condition: tt is at the bottom left corner of the house,
                   pen is up, and is facing up

    post-condition: tt is at the bottom right corner of the house,
                    pen is up, and is facing up
    """
    tt.color(color)
    tt.down()
    tt.right(90)
    tt.forward(100)
    tt.left(90)
    tt.forward(100)
    tt.left(45)
    tt.forward(math.sqrt(50**2 + 50**2))
    tt.left(90)
    tt.forward(math.sqrt(50**2 + 50**2))
    tt.left(45)
    tt.forward(100)
    tt.up()
    tt.left(90)
    tt.forward(100)
    tt.left(90)

    return 300 + 2 * math.sqrt(50**2 + 50**2)


def draw_grass():
    """
    draw_grass has the turtle draw the grass while also
    moving it to the next position for the next object

    returns: amount of ink to draw grass

    pre-condition: pen is up, and is facing up

    post-condition: pen is up, and is facing up
    """
    tt.color('Green')
    tt.down()
    tt.right(90)
    tt.forward(100)
    tt.left(90)
    tt.up()

    return 100


def draw_tree():
    """
    draw_tree randomly chooses a pine or maple tree to draw
    and then calls the appropriate function

    returns: amount of ink to draw tree
    """
    if random.randint(0, 1) == 1:
        return draw_pine_tree(random.randint(50, 200))
    else:
        return draw_maple_tree(random.randint(50, 150))


def main():
    """
    main asks the user if they want a house and if so what position
    it is in and what color it is. The forest scene is then drawn
    """
    wants_house = input("Is there a house in the forest (y/n)? ")

    if wants_house == "y":
        house_pos = input("At what position (1/2/3)? ")
        house_color = input("What color is the house? ")

    ink = 0
    tt.up()
    tt.back(250)
    tt.left(90)

    if wants_house == "n":
        ink += draw_grass()
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_grass()
    elif house_pos == "1":
        ink += draw_grass()
        ink += draw_house(house_color)
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
    elif house_pos == "2":
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_house(house_color)
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
    else:
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_tree()
        ink += draw_grass()
        ink += draw_house(house_color)
        ink += draw_grass()

    print("We used", ink, "units of ink for the drawing.")
    print("Close the diagram to end the program.")
    tt.done()


if __name__ == '__main__':
    main()
