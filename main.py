import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
color = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which tuttle will win the race? Enter a color:")

all_turtles = []

winning_line = Turtle()
winning_line.hideturtle()
winning_line.penup()
winning_line.goto(x=205, y=175)
winning_line.right(90)
winning_line.pensize(5)

while winning_line.ycor() > -150:
    winning_line.forward(10)
    winning_line.pendown()
    winning_line.forward(10)
    winning_line.penup()

y = -120
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    new_turtle.color(color[i])
    all_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won, winning color is {winning_color}")
            else:
                print(f"You've loose, winning color is {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()