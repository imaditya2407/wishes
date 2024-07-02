import turtle
import random
import time
from pygame import mixer

# Adding music is optional as per your choice.
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("happy-birthday-song.mp3")  # Add your music file name or path

# Set up the background
bg = turtle.Screen()
bg.bgcolor("black")
mixer.music.play()

# Draw lines
def draw_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(350)

draw_line(-170, -180)  # Bottom Line 1
draw_line(-160, -150)  # Mid Line 2
draw_line(-150, -120)  # First Line 3

# Draw the cake
turtle.penup()
turtle.goto(-100, -100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Draw candles
colors = ["red", "blue", "yellow", "green", "purple"]
for i in range(5):
    turtle.penup()
    turtle.goto(-90 + i * 30, 0)
    turtle.color(colors[i])
    turtle.pendown()
    turtle.forward(20)

# Decorate with circles
bg.bgcolor("orange")
for _ in range(7):
    angle = 360 / 7
    turtle.penup()
    turtle.goto(-40, -50)
    turtle.pendown()
    turtle.color(random.choice(colors))
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Display the birthday message
turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()
turtle.write(arg="Happy Birthday Purva!", align="left", font=("jokerman", 24, "normal"))

# Pause for a few seconds
time.sleep(5)

# Close the turtle graphics window
turtle.bye()
