import pandas

data=pandas.read_csv("weather_data.csv")
# print (data) #whole table AND automatically knows the first row is a header.
# print (data["day"][0]) #column "day". First value

# tota= sum(data["temp"].to_list())
# length= len(data["temp"])
# print (tota/length)
# -------the above is not needed if we use the following.
# print ("mean method:", data["temp"].mean())
# print ("max value:", data["temp"].max())

print (data.temp.max())





