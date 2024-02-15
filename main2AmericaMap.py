import turtle as tu
import main2Score as ans


screen1=tu.Screen()
image= "US-map.gif"
screen1.addshape (image)
tu.shape(image)

answer=ans.Score()

while len(answer.correct_guess_list)<50:

   ask = screen1.textinput(title=f"{len(answer.correct_guess_list)}/50 Guess the states Foo", prompt="Enter the state name").title()

   if ask== "Exit":
      answer.missed_list_f()
      break

   else:
      answer.check_ans(ask)

tu.mainloop()
