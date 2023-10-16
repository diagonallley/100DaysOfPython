MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

Money=0

is_machine_on=True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}ml
    Money: ${Money}
    """)

def resources_check(coffee):
    Water_rem=resources["water"]
    Milk_rem=resources["milk"]
    Coffee_rem=resources["coffee"]

    water_req=MENU[coffee]["ingredients"]["water"]
    milk_req=MENU[coffee]["ingredients"]["milk"]
    coffe_req=MENU[coffee]["ingredients"]["coffee"]

    if Water_rem<water_req:
        print("Sorry there is not enough water")
        return False
    elif Milk_rem<milk_req:
        print("Sorry there is not enough milk")
        return False
    elif Coffee_rem<coffe_req:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True 

# resources_check("espresso")
# report()

def process_coins(dimes,nickles,pennies,quarters, coffee):
    cost_coffee=MENU[coffee]["cost"]
    total_cost_dollars=0.25*quarters+0.10*dimes+0.01*pennies+0.05*nickles
    return total_cost_dollars

def process_transaction(coffee,total_cost):
    coffee_cost=MENU[coffee]["cost"]
    if coffee_cost < total_cost:
        balance= total_cost-coffee_cost
        print(f"Transaction Successful, here's your change {round(balance,2)}")
        return True
    elif coffee_cost==total_cost:
        print("Transaction Successful")
        return True
    elif coffee_cost>total_cost:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(coffee):
    milk_req=MENU[coffee]["ingredients"]["milk"]
    coffee_req=MENU[coffee]["ingredients"]["coffee"]
    water_req=MENU[coffee]["ingredients"]["water"]
    global Money
    resources["water"]-=water_req
    resources["coffee"]-=coffee_req
    resources["milk"]-=milk_req
    Money+=MENU[coffee]["cost"]
    print(f"Here is your {coffee}. Enjoy!")


def turn_off_machine():
   global is_machine_on
   is_machine_on=False


def coffee_process():
    user_choice=input("What would you like? (express/latte/cappuccino)").lower()
    global is_machine_on
    if user_choice=="off":
        is_machine_on=False
        
    else:    
        # break
        
        
        if user_choice=="espresso":
            resource_check=resources_check(user_choice)
        elif user_choice=="latte":
            resource_check=resources_check(user_choice)
        elif user_choice=="cappucino":
            resource_check=resources_check(user_choice)
        elif user_choice=="report":
            report()
            coffee_process()
        else:
            print("Enter something valid")
            coffee_process()
        

        if not resources_check:
            # continue
            coffee_process()
        else:
            print("Please insert coins:")
            quarters=float(input("How many quarters"))
            dimes=float(input("How many dimes"))
            nickles=float(input("How many nickles"))
            pennies=float(input("How many pennies"))
            total_cost=float(process_coins(dimes,nickles,quarters,quarters,user_choice))
            is_transaction=process_transaction(user_choice,total_cost)
            if is_transaction:
                make_coffee(user_choice)
            else:
                coffee_process()

while is_machine_on==True:
    coffee_process()
    



