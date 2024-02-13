import turtle as tu
import mainScore as ans


eog= False
screen1=tu.Screen()
image= "US-map.gif"
screen1.addshape (image)
tu.shape(image)

answer=ans.Name()

while eog==False:

   ask = screen1.textinput(title=f"{answer.count}/50 Guess the states Foo", prompt="Enter the state name").lower()

   answer.check_asn(ask)
   eog=answer.var

tu.mainloop()
