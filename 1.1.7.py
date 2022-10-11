#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles

direction=8
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.begin_fill()
  my_turtles.append(t)
  t.end_fill()
t.speed(0)
#  starts the code at this position
startx =0
starty =200

turtle_color = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

#  length of lines
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  new_color = turtle_color.pop()
  t.pencolor(new_color)
  t.right(16)     
  t.forward(50)
  direction=t.heading()

#	distane between shapes
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()