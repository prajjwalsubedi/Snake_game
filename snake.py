from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)
