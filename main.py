from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake1 = Snake()
snake1.head.color("white")
food = Food()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    #detect collision
    if snake1.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        #extend snake
        snake1.extend()
    # detect collision with wall
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        scoreboard.reset_score()
        snake1.reset()
    for block in snake1.blocks[1:]:
        if snake1.head.distance(block) < 10:
            snake1.reset()
            scoreboard.reset_score()

screen.exitonclick()
