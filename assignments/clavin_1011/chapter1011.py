#Author: Andrew Clavin
"""
 10.1.1
 Modify the recursive tree-growing function
 so that it branches at random angles between 10 and 60 degrees
 (instead of 30 degrees) and it shrinks the trunk/branch length
 by a random fraction between 0.5 and 0.75.
 Do your new trees now look more “natural”?
 """
import turtle
import random
def tree(tortoise, length, depth):
    if depth <= 1:
        tortoise.width(length / 9)
        tortoise.forward(length)
        tortoise.backward(length)
    else:
        randomDeg = random.uniform(10, 60)
        randomDeg2 = random.uniform(10, 60)
        randomDeg3 = random.uniform(10, 60)
        randomDega = random.uniform(10, 60)
        randomDeg2a = random.uniform(10, 60)
        randomDeg3a = random.uniform(10, 60)
        randomLength = random.uniform(0.15, 0.4)
        randomLength2 = random.uniform(0, 100)
        tortoise.width(length * randomLength / 5)
        tortoise.forward(length)
        tortoise.left(randomDeg)
        tree(tortoise, length * (randomLength), depth - 1)
        tortoise.right(randomDeg + randomDega)
        tree(tortoise, length * (randomLength), depth - 1)
        tortoise.left(randomDega)
        if (length > 190):
            tortoise.forward(randomLength2 / 10)
            tortoise.left(randomDeg / 2)
            tree(tortoise, length * randomLength, depth - 1)
            tortoise.right(randomDeg / 2)
            tortoise.backward(randomLength2 / 10)
        if (depth > 2):
            tortoise.backward(length / 3)
            tortoise.left(randomDeg2)
            tree(tortoise, length * (randomLength) * 1.3, depth - 1)
            tortoise.right(randomDeg2 + randomDeg2a)
            tree(tortoise, length * (randomLength * 1.3), depth - 1)
            tortoise.left(randomDeg2a)
            #tree(tortoise, length * randomLength * .75, depth - 2)
            tortoise.backward(length / 3)
            tortoise.left(randomDeg3)
            tree(tortoise, length * (randomLength) * 1.6, depth - 1)
            tortoise.right(randomDeg3 + randomDeg3a)
            tree(tortoise, length * (randomLength) * 1.6, depth - 1)
            tortoise.left(randomDeg3a)
            #tree(tortoise, length * randomLength * .75, depth - 2)
            tortoise.backward(length / 3)
        else:
            tortoise.backward(length)

def main():
    george = turtle.Turtle()
    murtle = turtle.Turtle()
    reese = turtle.Turtle()
    george.speed(0)
    george.left(90)
    george.penup()
    george.backward(200)
    george.pendown()
    tree(george, 200, 6)
    """
    murtle.speed(0)
    murtle.penup()
    murtle.forward(300)
    murtle.left(90)
    murtle.backward(200)
    murtle.pendown()
    tree(murtle, 200, 5)
    reese.speed(0)
    reese.penup()
    reese.backward(310)
    reese.left(90)
    reese.backward(200)
    reese.pendown()
    tree(reese, 200, 5)
    """
    #screen = george.getscreen()
    #screen.exitonclick()

main()
