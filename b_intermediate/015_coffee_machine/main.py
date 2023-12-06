MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

###

in_use = True
balance = 0

###

def report():
  '''Prints the amounts of resources available and current money balance'''
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${balance}")

def is_resource_available(ingredients):
  '''Checks whether a product can be made based on available resources'''
  for item in ingredients:
    if ingredients[item] >= resources[item]:
      print(f"Sorry, there is not enough {item}")
      return False
    return True

def take_coins():
  '''Returns the total value of inserted coins'''
  print("Please insert coins.")
  quarters = int(input("How many quarters? "))
  dimes = int(input("How many dimes? "))
  nickels = int(input("How many nickels? "))
  pennies = int(input("How many pennies? "))
  return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

def is_transaction_successful(money_inserted, product_price):
  '''Indicates whether the customer has inserted enough coins to complete the order'''
  if money_inserted >= product_price:
    change = round(money_inserted - product_price, 2)
    global balance
    balance += product_price
    if change:
      print(f"Here's your ${change} change")
    return True
  else:
    print("Sorry, that's not enough money. Refunding...")
    return False

def make_coffee(product, ingredients):
  '''Deduct required ingredients from resources'''
  for item in ingredients:
    resources[item] -= ingredients[item]
  print(f"Here's your {product}. Enjoy!")

###

while in_use:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    print("Bye bye!")
    in_use = False
  elif choice == "report":
    report()
  else:
    product = MENU[choice]
    if is_resource_available(product["ingredients"]):
      payment = take_coins()
      if is_transaction_successful(payment, product["cost"]):
        make_coffee(choice, product["ingredients"])