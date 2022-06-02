#Setup code
import random
import turtle as t
screen = t.Screen()
screen.setup(width = 500,height= 400)
screen.bgcolor("black")
racecolors = ["Red","Orange","Yellow","Green","Blue","Purple","HotPink"]
y_positions=[-100,-70,-40,-10,20,50,80]

#Racing code
myturtle = screen.textinput("Welcome to my turtle racing game!", "Choose your turtle color: ")
all_turtles = []

for turtleindex in range(0,7):
  turtle= t.Turtle("turtle")
  turtle.penup()
  turtle.color(racecolors[turtleindex])
  turtle.goto(x=-220,y=y_positions[turtleindex])
  all_turtles.append(turtle)
is_race_on = True
while is_race_on:
  for turtle in all_turtles:
    random_distance=random.randint(0,5)
    turtle.forward(random_distance)
    if turtle.xcor() > 220:
      is_race_on = False
      winningturtle = turtle.pencolor()
      if winningturtle == myturtle:
        print(f"You won!{winningturtle} wins! Thanks for playing!")
      else:
        print(f"You lose! The winning turtle is {winningturtle}! Better luck next time!")
