#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.goto(-250,300)
letters = ["a","s","d","f","g","h","j","k","l"]
pears = []





#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()


for step in range(5):
  apple = trtl.Turtle()
  pears.append(apple)
  draw_apple(apple)
  apple.penup()
  apple.goto(rand.randint(-150,150),rand.randint(0,150))
  

popped = letters.pop(rand.randint(0,8))
print(popped)




def draw_an_A():
  drawer.color("blue")
  drawer.write(popped, font=("Arial", 74, "bold"))

def drop():
  draw_an_A()
  orange =pears.pop(rand.randint(0,4))
  xcor=orange.xcor()
  orange.goto(xcor,-150)
  drawer.clear()

wn.onkeypress(drop, popped)
#-----function calls-----

  
wn.listen()
wn.mainloop()