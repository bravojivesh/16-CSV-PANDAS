import turtle as tu
import pandas

data= pandas.read_csv("50_states.csv")
print (data)
data_dict= data.to_dict()

# print(data_dict)
# print (data_dict['state'][0])
# print (data_dict["x"][0], data_dict["y"][0])


class Name(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.var=False #to pass to main.py so that eog can be updated correctly.
        self.count= 0 #this should be an attribute as we need this outside of mehod calls. The method check_ans will be called multple times

    def check_asn(self,answer):
        string=""
        x1,y1=0,0
        flag=0 #need to keep track if the user entered correct answer. It will only become 1, if it matched with the list.
        # print("Parameter for the function:", answer)
        for ind in range (0,50,1):
            state_name= (data_dict['state'][ind]).lower()
            if answer == state_name:
                string=(answer).upper()
                x1= data_dict['x'][ind]
                y1=data_dict['y'][ind]
                self.goto(x1,y1)
                self.write(f"{string}", False, align="right", font="Arial")
                # print ("from inside the correct logic block", answer, string)
                self.count +=1
                flag=1
            # else:
            #     pass
            #JH: I had this block earlier. I completely forgot that we are comparing with each element of the list, and will always trigger.
            # so to keep the flag inside "else" would be meaningless.
        if flag !=1:
           self.var=True





