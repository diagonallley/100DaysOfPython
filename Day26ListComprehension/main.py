# List comprehension

numbers=[0,1,2,3,4,5,6]

new_list=[n*2 for n in numbers]

print(new_list)


newstring="This is the string"

string_list=[st for st in newstring]
print(string_list)


new_nums=[n*2 for n in range(0,5)]

print(new_nums)

# Conditional list comprehension

names=["Ren", "Beth", "Rudo","Bruno","Noell","Emmet","Eloise","Elaine","Regetha", "Inegear"]

s_names=[name for name in names if len(name)<9]

print(s_names)

l_names=[name.upper() for name in names if len(name)>5]

print(l_names)