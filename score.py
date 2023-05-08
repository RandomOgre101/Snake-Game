from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(0,260)
        self.hideturtle()
        self.write_score()
        

    def write_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", False, align=ALIGN, font=('Arial', 18, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()