from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

cont = True
while cont:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        cont = False
        score.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            cont = False
            score.game_over()


screen.exitonclick()
