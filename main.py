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
    time.sleep(0.1)

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        point.print_score()

screen.exitonclick()
