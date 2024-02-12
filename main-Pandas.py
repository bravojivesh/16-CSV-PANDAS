import pandas

data=pandas.read_csv("weather_data.csv")
# print (data) #whole table AND automatically knows the first row is a header.
# print (data["day"][0]) #column "day". First value

# print (data)

# tota= sum(data["temp"].to_list())
# length= len(data["temp"])
# print (tota/length)
# -------the above is not needed if we use the following.
# print ("mean method:", data["temp"].mean())
# print ("max value:", data["temp"].max())

# print (data.temp.max()) #prints maximum value in temp column
x= data[data.day=="Monday"] #prints row(s) where day is Monday
y = data[data.condition== "Sunny"] #prints row(s) where condition is Sunny. You will get multiple rows

print (x.condition)





