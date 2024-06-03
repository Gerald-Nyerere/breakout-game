from turtle import Turtle

score= 0

class Scoredboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        #CREATING THE scoreboard 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highscore = score
        self.goto(x=580, y = 260)
        self.lives = lives
        self.score = 0
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score: {self.score}  | Highest Score {self.highscore} | Lives: {self.lives} |", align="center", font=("Courier", 80, "normal"))
       

        

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
             self.highscore += 1
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()
        open('highestScore.text', 'w').write(str(self.highscore)) 
       

