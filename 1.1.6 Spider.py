#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
leg_length = 120

leg_angle = 200 / legs
spider.pensize(5)
remaining = 0
while (remaining < legs):
  spider.goto(0,0)
  spider.setheading(leg_angle*remaining)
  spider.forward(leg_length)
  remaining = remaining + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()