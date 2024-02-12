import pandas as pd

sq_data= pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count=len(sq_data[sq_data["Primary Fur Color"]== "Gray"])
cin_count=len(sq_data[sq_data["Primary Fur Color"]== "Cinnamon"])
black_count=len(sq_data[sq_data["Primary Fur Color"]== "Black"])

#=====================================
# gray_count, cin_count, black_count=0,0,0
#
# for color in all_color:
#     if color== "Gray":
#         gray_count+=1
#     elif color=="Cinnamon":
#         cin_count+=1
#     else:
#         black_count +=1
#================================================

list=[gray_count,cin_count,black_count]
dict= {"Fur Color": ["Gray", "Cinnamon", "Black"],
       "Count": list
       }

# print (list)
# print (dict)

df1=pd.DataFrame(dict)
print(df1)
df1.to_csv("jh-result.csv")


