from os import path
 
FILE_NAME = "high_score.txt"
HEART_SYMBOL = "💛"
 
 
class Game:
 
    def __init__(self):
        if path.exists(FILE_NAME):
            with open(FILE_NAME, mode="r+") as score_file:
                score_string = score_file.read().strip("\r\n")
                if len(score_string) > 0:
                    self.high_score = int(score_string)
                else:
                    self.high_score = 0
        else:
            open(file=FILE_NAME, mode="x")
            self.high_score = 0
        self.score = 0
        self.lives = 5
 
    def remaining_hearts(self):
        hearts = ""
        for _ in range(self.lives):
            hearts += HEART_SYMBOL
        return hearts
 
    def high_score_check(self):
        if self.score > self.high_score:
            with open(FILE_NAME, mode="w+") as score_file:
                score_file.write(f"{self.score}")