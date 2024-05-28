from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        self.check_finish()

    def create_turtle(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90) # Point the turtle upwards

    def move_up(self):
        if self.heading() == 90:
            self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def check_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False


