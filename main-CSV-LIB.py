import csv

# with open ("weather_data.csv") as data_file:
#     content= csv.reader(data_file)
#     temp=[]
#     for row in content:
#         x= row[1]
#         temp.append(x)
#     new_temp=temp[1:]
#     final_temp=[]
#     for x in new_temp:
#         x1=int(x)
#         final_temp.append(x1)
#     print(final_temp)
#----------------WAY 1: ABOVE

with open ("weather_data.csv") as data_file:
    content= csv.reader(data_file)
    temp=[]
    for column in content: #all columns
        temp_col=column[1] #second column only-- the ones with temperature
        if temp_col== "temp":
            pass
        else:
            x1=int(temp_col)
            temp.append(x1)
    print (temp)
    #--------------------WAY 2 ABOVE


