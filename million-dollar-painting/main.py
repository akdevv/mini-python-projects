import random
from turtle import Screen, Turtle

# colors form Hirst's sample painting
colors = [(135, 164, 199), (223, 152, 103), (31, 43, 61), (202, 136, 147),
          (162, 60, 50), (235, 212, 93), (50, 101, 142), (137, 181, 162),
          (146, 64, 72), (55, 49, 46), (158, 33, 30), (61, 115, 100),
          (167, 30, 34), (229, 165, 170), (35, 60, 54), (235, 166, 157),
          (211, 86, 76), (53, 41, 44), (15, 97, 69), (34, 60, 105),
          (171, 186, 220), (193, 100, 109), (108, 127, 157), (17, 86, 105),
          (36, 149, 207), (174, 200, 190)]

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.penup()
tim.speed("fast")
tim.hideturtle()

# set initial position of turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, 101):
    # draw the dots
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    # change to next line
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# keep the window open
screen.exitonclick()
