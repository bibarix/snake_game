import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake body
segments = []

# Food for the snake
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Functions to control the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def check_collision_with_food():
    if head.distance(food) < 20:
        return True
    return False

def check_collision_with_border():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True
    return False

def check_collision_with_self():
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    return False

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Main game loop
while True:
    screen.update()

    if check_collision_with_border():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Reset the segments list
        for segment in segments:
            segment.goto(1000, 1000)  # Move the segments out of screen
        segments.clear()

    if check_collision_with_self():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        
        # Reset the segments list
        for segment in segments:
            segment.goto(1000, 1000)  # Move the segments out of screen
        segments.clear()

    if check_collision_with_food():
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

    # Move the segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(0.1)

screen.mainloop()
s