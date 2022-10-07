from turtle import Screen
from snake import Snake
from food import Food
from points import Point
import time

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
point = Point()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    snake.move()
    screen.update()
    time.sleep(0.12)

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        point.print_score()

    if snake.segments[0].xcor() < -280 or snake.segments[0].xcor() > 280 or snake.segments[0].ycor() < -280 \
            or snake.segments[0].ycor() > 280:
        point.print_over()
        is_game_on = False

    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            point.print_over()
            is_game_on = False

screen.exitonclick()
