#Emmet

#import statements
import turtle as trtl
import random as rand
import time
#game setup
#initiate turtles
barrier=trtl.Turtle()
sc = trtl.Turtle()
ship=trtl.Turtle()
counter=trtl.Turtle()
wn=trtl.Screen()

#font setup
font_setup=("Comic Sans", 20, "bold")

#barrier setup
barrier.shape("circle")
barrier.turtlesize(1)

#counter setup
counter.hideturtle()
counter.penup()
counter.goto(200,250)

#Jackson
#timer
timer = 30
counter_interval=1000
timer_up=False

#score
score=0
sc.penup()
sc.hideturtle()
sc.goto(-250,250)
sc.write("Score: " +str(score),font=font_setup)
#lists
bullet_fired=[]
barrier_shot=[]

#Emmet
#ship setup
def turn_left():
    turn_left=ship.left(2)
def turn_right():
    turn_right=ship.right(2)
ship.shape("classic")
ship.color("blue")
wn.onkeypress(turn_left,"a")
wn.onkeypress(turn_right,"d")
wn.listen()
ship_alive=True

#Emmet
#funcitons
def update_score():
    global score
    score += 1 
    sc.clear()
    (sc.write("Score: " +str(score),font=font_setup))
#Emmet and Jackson
def shoot():
    global bullet
    bullet=trtl.Turtle()
    bullet.shape("circle")
    bullet.turtlesize(1-0.7)
    bullet.speed(0)
    bullet.color("#ff0000")
    b_angle=ship.heading()
    bullet.setheading(b_angle)
    for step in range(50):
        bullet.forward(10)
        if (abs(bullet.pos() - barrier.pos())<5):
            update_score()
            bar_g()
    bullet.hideturtle()
    bullet.clear()

#Jackson
def countdown():
    global timer, timer_up
    counter.clear()
    if timer<=0:
        counter.write("timer up",font=font_setup)
        timer_up=True
        counter.hideturtle()
    else:
        counter.write("timer: " + str(timer), font=font_setup)
        timer-=1
        counter.getscreen().ontimer(countdown, counter_interval)
#Jackson
def bar_g():
    for step in range(100):
        barrier.penup()
        random_angles=rand.randint(1,360)
        rand_x=rand.randint(-200,200)
        rand_y=rand.randint(-300,300)
        barrier_shot.append(barrier)
        for step in range (100):
            barrier.penup()
            barrier.setheading(random_angles)
            barrier.goto(rand_x,rand_y)
            



#Emmet
#events
wn.ontimer(countdown, counter_interval)
wn.onkey(shoot,"w")
time.sleep(0.2)
bar_g()


print (score)
wn.bgcolor("white")
wn.mainloop()
