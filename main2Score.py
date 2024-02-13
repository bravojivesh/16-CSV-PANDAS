import turtle as tu
import pandas

data=pandas.read_csv("50_states.csv")
# print (data["state"])
class Score(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.list=[]

    def check_ans(self,answer):
        states= data["state"].tolist()
        print(states)
        if answer.lower() in states:
                get_row=data[data.state==x] #gets the entire row with index and data type info
                x_cor=int(get_row.x.item())
                y_cor=int(get_row.y.item())
                self.goto(x_cor,y_cor)
                self.write(answer.title())





s=Score()
s.check_ans("North Carolina")



