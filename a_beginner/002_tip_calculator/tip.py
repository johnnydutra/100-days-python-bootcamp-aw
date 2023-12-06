print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip_rate = input("What percentage tip would you like to give? ")
party_size = input("How many people are splitting the bill? ")

after_tip = float(total_bill) * (1 + (int(tip_rate) / 100))

# round will not fit digits ending in 0 properly
pay_per_person = round(after_tip / int(party_size), 2)
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay ${pay_per_person}")