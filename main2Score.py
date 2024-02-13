import turtle as tu
import pandas

data=pandas.read_csv("50_states.csv")
# print (data["state"])
class Score(tu.Turtle):
    def __init__(self):
        super().__init__()
    def check_ans(self,answer):
        states= data["state"]
        for x in states:
            if answer== x:
                p=data[data.state==x]
                px=p.x
                print (px)





s=Score()
s.check_ans("Texas")

