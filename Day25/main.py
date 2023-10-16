# with open('weather_data.csv') as data:
#     list=data.readlines()

# print(list)


# import csv

# with open('./weather_data.csv') as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     data_list=list(data)
#     for i in range(1,len(data_list)):
       
#         temperatures.append(int(data_list[i][1]))
#     print(temperatures)

import pandas

data=pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data)
# print(data["temp"])

# The whole table is a df and a single column is a series


#Converting to a dictionary
# data_dictionary=data.to_dict()
# print(data_dictionary)

#Series to a list
list=data["temp"].to_list()
average_temp=sum(list)/len(list)

#Using series mean method

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

#Getting row data from the file

row=data[data.day=="Monday"]
# print(row)

max_temp_row=data[data.temp==data.temp.max()]
monday=data[data.day=="Monday"]
print((monday.temp*1.8)+32)
# print(max_temp_row)