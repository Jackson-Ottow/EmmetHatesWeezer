#-----import statements-----
import turtle as trtl
import turtle as trtl2
import turtle as trtl3
import random as rand
#-----game configuration----
tcolor = "red"
psize = 2
shape = "circle"
score = 0
swx=0
swy=250
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
t = trtl.Turtle()
t.fillcolor(tcolor)
t.pensize(psize)
t.shape(shape)

sw = trtl2.Turtle()
sw.penup()
sw.hideturtle()
sw.goto(swx+50,swy)

counter = trtl3.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(swx-100,swy)
#-----game functions--------
def t_clicked(x, y):
    global timer
    if timer_up >=0:
        update_score()
        change_pos()
    else:
        counter.hideturtle()
  
def change_pos():
    new_xpos = rand.randint(-300,300)
    new_ypos = rand.randint(-250,250)
    t.penup()
    t.hideturtle()
    t.goto(new_xpos,new_ypos)
    t.showturtle()

def update_score():
    global score
    score += 1 
    sw.clear()
    (sw.write(score,font=font_setup))

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
t.onclick(t_clicked)
wn = trtl.Screen()
wn.bgcolor("purple")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()