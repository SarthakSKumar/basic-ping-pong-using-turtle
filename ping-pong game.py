"""
# Ping Pong Game using Turtle
# Last Updated: 20:52 10/02/2022
# Last Updated by: Sarthak S Kumar
# Changes to be committed: --> Addition of Endgame Function in the program to display winner and exit
"""

import turtle
import time
# Window
wind = turtle.Screen()
wind.title('CTXGO')
wind.bgcolor('green')
wind.setup(width=800, height=600)
wind.tracer(0)

# Bar A
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('black')
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.penup()
bar_A.goto(-350, 0)

# Bar B
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('black')
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.penup()
bar_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball_x = 0.2
ball_y = 0.2

# score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write("Player A: 0 Player B: 0", align="center",
             font=("Courier", 24, 'normal'))

score_a = 0
score_b = 0


# Functions
def bar_A_up():
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)


def bar_A_down():
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)


def bar_B_up():
    y = bar_B.ycor()
    y += 30
    bar_B.sety(y)


def bar_B_down():
    y = bar_B.ycor()
    y -= 30
    bar_B.sety(y)


# Keyboard Bindings
wind.listen()
wind.onkeypress(bar_A_up, 'w')
wind.onkeypress(bar_A_down, 's')
wind.onkeypress(bar_B_up, 'Up')
wind.onkeypress(bar_B_down, 'Down')

"""Function to show the winner screen
    --> Called when either of the scores reaches 10, in the __main__"""


def endgame():
    sc = turtle.Screen()
    sc.title('Winner!')
    sc.bgcolor('orange')
    sc.setup(width=400, height=300)
    sc.tracer(0)
    win = turtle.Turtle()
    win.color('black')
    win.penup()
    win.goto(0, 50)
    if score_a > score_b:
        win.write("Player A wins!! Congrats", align="center",
                  font=("Courier", 10))
    else:
        win.write("Player B wins!! Congrats", align="center",
                  font=("Courier", 10))
    win.hideturtle()
    time.sleep(5)
    exit()


while True:
    wind.update()

    # BAll movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1

    # score
    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("Player A: {} Player B {}".format(
            score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1
    if ball.xcor() < -350:
        score_b += 1
        sboard.clear()
        sboard.write("Player A: {} Player B {}".format(score_a, score_b), align='center',
                     font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1

    # Collision with bars

    if ball.xcor() < -340 and ball.ycor() < bar_A.ycor() + 50 and ball.ycor() > bar_A.ycor() - 50:
        ball_x *= -1
    if ball.xcor() > 340 and ball.ycor() < bar_B.ycor() + 50 and ball.ycor() > bar_B.ycor() - 50:
        ball_x *= -1

    """Selection statement to check if either of the scores are equal to 10"""
    if score_a == 10 or score_b == 10:
        endgame()
