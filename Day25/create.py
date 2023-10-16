import pandas

# Create a df from scratch
data_dict={
    "students":["Amy","James","Jack"],
    "scores":[76,77,78]
}

data=pandas.DataFrame(data=data_dict)
data.to_csv("newdata.csv")

print(data)