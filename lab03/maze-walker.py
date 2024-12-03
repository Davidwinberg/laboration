import maze
import turtle

def turtle_start(turtle, pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.left(90)
    turtle.pendown()





def turn_left(grader):
    ninja.left(90)
    grader += 90
    ninja.forward(1)

def turn_right(grader):
    ninja.right(90)
    grader -= 90


def walk_straight(grader):
    while walker.wall_in_front(grader, ninja.pos()) == False and walker.wall_at_left(grader, ninja.pos()) == True:
        ninja.forward(1)






def main():
    grader = 90

    while walker.at_exit(ninja.pos()) != True:

        walk_straight(grader)
        # Turn right
        if walker.wall_in_front(grader, ninja.pos()) == True and walker.wall_at_left(grader, ninja.pos()) == True:
            ninja.right(90)
            grader -= 90

        # Turn left
        elif walker.wall_in_front(grader, ninja.pos()) != True and walker.wall_at_left(grader, ninja.pos()) != True:
            ninja.left(90)
            grader += 90
            ninja.forward(1)

#Maze
user_maze = int(input("Pick a maze [1-5]: "))
walker = maze.Maze(user_maze)
entry = walker.entry()
#Turtle
ninja = turtle.Turtle()
ninja.shape('turtle')
ninja.shapesize(0.5)
turtle_start(ninja, entry)


if user_maze == 5:
    turtle.Screen().delay(1)
    turtle.Screen().tracer(2)
    main()
else:
    main()
turtle.mainloop()