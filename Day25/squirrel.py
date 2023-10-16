import pandas
data=pandas.read_csv('squirrel.csv')

grey_count=0
red_count=0
black_count=0

colors_list=data["Primary Fur Color"].to_list()
for color in colors_list:
    if color=="Gray":
        grey_count+=1
    elif color=="Cinnamon":
        red_count+=1
    elif color=="Black":
        black_count+=1

print(grey_count,black_count,red_count)

# Fur Color Count

color_dict={"Fur Color":["grey","red","black"],"Count":[grey_count,red_count,black_count]}

color_count=pandas.DataFrame(color_dict)
color_count.to_csv('squirrelColors.csv')