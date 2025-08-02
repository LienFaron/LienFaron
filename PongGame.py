# Simple Pong game in Python 3 using the Turtle module
# By Gemini

import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Stops the window from updating automatically

# --- Game Objects ---

# Paddle A (Left)
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Max animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch shape to be a paddle
paddle_a.penup()  # Doesn't draw a line when moving
paddle_a.goto(-350, 0)  # Start position

# Paddle B (Right)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
# Ball movement speed can be adjusted here
ball.dx = 0.15  # Delta x (change in x)
ball.dy = 0.15  # Delta y (change in y)

# --- Score System ---
score_a = 0
score_b = 0

# Pen for drawing the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # We don't need to see the turtle, just its writing
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# --- Functions to move paddles ---

def paddle_a_up():
    y = paddle_a.ycor()  # Get current y-coordinate
    if y < 250:  # Prevent paddle from going off-screen
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)

# --- Keyboard bindings ---
wn.listen()  # Tell the window to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# --- Main Game Loop ---
while True:
    wn.update()  # Manually update the screen in each loop iteration

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (Top and Bottom walls)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse the y-direction
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Border checking (Left and Right walls - Scoring)
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Reset ball to center
        ball.dx *= -1  # Reverse direction for the other player
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # Paddle B (Right)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # Paddle A (Left)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1