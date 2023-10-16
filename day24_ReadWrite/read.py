# file=open("day24_ReadWrite\\newtext.txt")

# contents=file.read()

# print(contents)

# file.close()



# with open('day24_ReadWrite\\newtext.txt') as file:
#     contents=file.read()
#     print(contents)

# r is read, w is write, and a is append


# with open('day24_ReadWrite\\newtext.txt', mode="w") as file:
#     file.write("New text that is about to be written")

with open('day24_ReadWrite\\newtext.txt', mode="a") as file:
    file.write("\nNew text that is about to be written")

# if we open a file in write mode, and that file does not exist, a new file will get created with the name

with open('day24_ReadWrite\\writetext.txt', mode="w") as file:
    file.write("New file write")