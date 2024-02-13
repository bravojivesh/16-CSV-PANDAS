import turtle as tu
import main2Score as ans


eog= False
screen1=tu.Screen()
image= "US-map.gif"
screen1.addshape (image)
tu.shape(image)

answer=ans.Score()

while eog==False:

   ask = screen1.textinput(title=f"/50 Guess the states Foo", prompt="Enter the state name").lower()

   answer.check_ans(ask)
   # eog=answer.var

tu.mainloop()
