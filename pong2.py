import turtle


wn = turtle.Screen()
wn.title("Pong Revised")
wn.bgcolor("gray")
wn.setup(height = 800, width = 600)
wn.tracer(0)

# Paddle A
Paddle_A = turtle.Turtle()
Paddle_A.shape("square")
Paddle_A.speed(0)
Paddle_A.color("black")
Paddle_A.penup()
Paddle_A.goto(-350, 0)
Paddle_A.shapesize(stretch_wid = 5, stretch_len = 1)

# Paddle B
Paddle_B = turtle.Turtle()
Paddle_B.shape("square")
Paddle_B.speed(0)
Paddle_B.color("black")
Paddle_B.penup()
Paddle_B.goto(350, 0)
Paddle_B.shapesize(stretch_wid = 5, stretch_len = 1)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("black")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 2
Ball.dy = -2

def Paddle_A_up():
    y = Paddle_A.ycor()
    y += 20
    Paddle_A.sety(y)

def Paddle_A_down():
    y = Paddle_A.ycor()
    y -= 20
    Paddle_A.sety(y)

def Paddle_B_up():
    y = Paddle_B.ycor()
    y += 20
    Paddle_B.sety(y)

def Paddle_B_down():
    y = Paddle_B.ycor()
    y -= 20
    Paddle_B.sety(y)







    # Keyboard Bindings
wn.listen()
wn.onkeypress(Paddle_A_up, "w")
wn.onkeypress(Paddle_A_down, "s")
wn.onkeypress(Paddle_B_up, "Up")
wn.onkeypress(Paddle_B_down, "Down")







while True:
    wn.update()


    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1

    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Paddle_B.ycor() + 40 and Ball.ycor() > Paddle_B.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Paddle_A.ycor() + 40 and Ball.ycor() > Paddle_A.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1
