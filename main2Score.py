import turtle as tu
import pandas

data=pandas.read_csv("50_states.csv")
states= data["state"].tolist() #covert to list. In my other version, it is dictionary.

class Score(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.correct_guess_list=[]
        self.missed_list=[]

    def check_ans(self,answer0):
        answer= answer0.title()
        # if answer.lower() in (state.lower() for state in states):
        # this will not work because everything in
        # the state list is title case.
        #if we change to lower and compare, it will work for comparison ONLY.To get the cordinates, we have to use
        # the same case as in the csv. So we have to change the input to title case.

        if answer in states:
                get_row=data[data.state==answer] #gets the entire row with index and data type info
                x_cor=int(get_row.x.item()) #getting only the value from x and changing it to int.
                y_cor=int(get_row.y.item()) #same as above for y.
                self.goto(x_cor,y_cor) #after values are in int, telling the turtle to go to write cordinate.
                self.write(answer.title())
                # print (answer, x_cor, y_cor)
                self.correct_guess_list.append(answer)
                # print(self.correct_guess_list) #debuggin only:

    def missed_list_f(self): #made a mistake of using the same name for function and attribute
        # for x in states:
        #     if x not in self.correct_guess_list:
        #         self.missed_list.append(x)

        #Either the above Or below. The one below is with list comprehension.

        self.missed_list= [x for x in states if x not in self.correct_guess_list]

        df=pandas.DataFrame(self.missed_list)
        df.to_csv("Missed_state.csv")








# s=Score()
# s.check_ans("Ohio")



