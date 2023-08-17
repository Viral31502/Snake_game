from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]


    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new_block = Turtle("square")
        new_block.color("grey")
        new_block.penup()
        new_block.setpos(position)
        self.blocks.append(new_block)

    def extend(self):
        self.add_segment(self.blocks[-1].position())

    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for block in self.blocks:
            block.goto(1000,1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
        self.head.color("white")
