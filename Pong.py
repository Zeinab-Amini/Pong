import turtle
import time
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("medium orchid")
screen.setup(900, 800, starty=-20)
screen.tracer(0)
stick1 = turtle.Turtle()
stick1.color("blue")
stick1.shape("square")
stick1.shapesize(15, 1)
stick1.penup()
stick1.goto(-300, 0)
stick2 = turtle.Turtle()
stick2.color("red")
stick2.shape("square")
stick2.shapesize(15, 1)
stick2.penup()
stick2.goto(300, 0)
ball = turtle.Turtle()
ball.color("green")
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.dx = 0.25
ball.dy = 0.25


def upkey():
    y = stick1.ycor()
    stick1.sety(y + 15)


def downkey():
    y = stick1.ycor()
    stick1.sety(y - 15)


def wkey():
    y = stick2.ycor()
    stick2.sety(y + 15)


def skey():
    y = stick2.ycor()
    stick2.sety(y - 15)


screen.onkey(upkey, "Up")
screen.onkey(downkey, "Down")
screen.onkey(wkey, "w")
screen.onkey(skey, "s")
screen.listen()

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Blue Score:0  Red Score:0",align="center",font=("Times New Roman",23,"normal"))
Blue_Score = 0
Red_Score = 0
while True:
    screen.update()
    x = ball.xcor()
    ball.setx(x + ball.dx)
    y = ball.ycor()
    ball.sety(y + ball.dy)
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy = -1 * ball.dy
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy = -1 * ball.dy
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx
        time.sleep(1.5)
        Blue_Score=Blue_Score+1
        pen.clear()
        pen.write("Blue Score={}, Red Score={}".format(Blue_Score, Red_Score), align="center",
                  font=("Times New Roman", 24, "normal"))
    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx
        time.sleep(1.5)
        Red_Score=Red_Score+1
        pen.clear()
        pen.write("Blue Score={}, Red Score={}".format(Blue_Score, Red_Score), align="center",
                  font=("Times New Roman", 24, "normal"))
    if ball.xcor() > 290 and ball.ycor() < 150 + stick2.ycor() and ball.ycor() > -150 + stick2.ycor():
        ball.dx = -1 * ball.dx
    if ball.xcor()<-290 and ball.ycor()<150+stick1.ycor() and ball.ycor()>-150+stick1.ycor():
        ball.dx=-1*ball.dx
    if Blue_Score==10 or Red_Score==10:
        screen.bye()