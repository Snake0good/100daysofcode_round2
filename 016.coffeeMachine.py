import time

################
### menu.py ####
################
class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drinks(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available")




########################
### coffee_maker.py ####
########################
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        time.sleep(1)
        print(f"Water: {self.resources['water']}ml")
        time.sleep(1)
        print(f"Milk: {self.resources['milk']}ml")
        time.sleep(1)
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry, there is not enough {item}.")
                can_make = False
        return can_make

    
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕ Enjoy!\n") 




#########################
### money_machine.py ####
#########################
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"\nProfit: {self.CURRENCY} {round(self.profit, 2)}\n")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"\nHow many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            time.sleep(1)
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {self.CURRENCY}{change} in change.\n")
            self.profit += cost 
            self.money_received = 0
            return True
        else:
            time.sleep(1)
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False

########################
### main.py ####
########################
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappucino = MenuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

on = True
while on:
    print("What would you like? Our menu includes...")
    time.sleep(0.75)
    print("-- espresso --")
    time.sleep(0.75)
    print("-- latte --")
    time.sleep(0.75)
    print("-- cappuccino --")
    time.sleep(0.75)
    print("(type 'off' or 'report' for more options)")
    time.sleep(0.75)
    choice = input("Please choose: ")

    if choice == "off":
        print("Have a great day!")
        on = False
    elif choice == 'report':
        password = input("Please enter the password: ")
        if password == '123abc':
            coffee_maker.report()
            money_machine.report()
        else:
            print("\nSorry, that password is incorrect\n")
            time.sleep(2)
            pass
    else:
        coffee_choice = menu.find_drinks(choice)
        if coffee_maker.is_resource_sufficient(coffee_choice) and money_machine.make_payment(coffee_choice.cost):
            coffee_maker.make_coffee(coffee_choice)