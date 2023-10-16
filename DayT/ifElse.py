print("Welcome to the rollercoaster!")

height=int(input("What is your height in cm? "))

# if height>=120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you cannot ride this ride.")

#Everything that is indented after the if or else keyword is a block of code


#Nested if else condition

if height>=120:
    age=int(input("What is your age?"))
    if age>18:
        print("Please pay $12.")
    elif age>=12 and age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $5.")
else:
    print("Sorry you cannot ride the rollercoaster")