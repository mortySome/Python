print("Welcome to the tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))

total_bill = int(tip) / 100 * bill + bill

people_bill = total_bill / no_of_people

roundoff = round(people_bill, 2)

print(f"Each person should pay: ${roundoff}")



