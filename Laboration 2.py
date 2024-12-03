import turtle
import random

def move_turtle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def random_step(turtle):
    steps = random.randint(5, 15)
    turtle.forward(steps)
    direction = random.randint(1, 2)
    if direction == 1:
        turtle.left(45)
    elif direction == 2:
        turtle.right(45)




def random_walk(turtle, n):
    for x in range(n):
        random_step(turtle)


def main():
    turtle.Screen().delay(0)

    ninja1 = turtle.Turtle()
    ninja2 = turtle.Turtle()
    turtle.Screen().bgcolor('magenta')
    ninja1.pencolor('green')
    move_turtle(ninja1, -50, -50)
    move_turtle(ninja2, 50, 50)

    while ninja1.distance(ninja2) > 100:
        random_step(ninja1)
        random_step(ninja2)
main()





turtle.mainloop()


