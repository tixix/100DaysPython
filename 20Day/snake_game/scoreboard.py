from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, self.screen.window_width() // 2 - 30)
        self.color('white')
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
