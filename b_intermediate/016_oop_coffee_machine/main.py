# from turtle import Turtle, Screen

# leo = Turtle()
# print(leo)
# leo.shape("turtle")
# leo.color("red")
# leo.forward(100)

# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"])
# table.add_column("Pokemon Type", ["Grass/Poison", "Fire", "Water", "Electric"])
# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


in_use = True

while in_use:
  options = menu.get_items()
  choice = input(f"What would you like? ({options})")
  if choice == "off":
    in_use = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
