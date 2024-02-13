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
   # print("user entered:",ask)
   answer.check_asn(ask)
   eog=answer.var


# # def get_mouse_click_coor(x,y):
# #    print (x,y)
# tu.onscreenclick(get_mouse_click_coor)

#JH: the above was for information only. Event listener method that will display the coordinates, when we clicked.

tu.mainloop()

#screen1.exitonclick() #this is wrong for this project, as we DO NOT WANT TO EXIT when clicked on the screen.