# Project Tip Calculator

# Write your code below this line 👇
print("Welcome to the tip calculator. ")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
split_the_bill = int(input("How many people to split the bill? "))

tip_calculation = ((total_bill * tip_percentage / 100) + total_bill) / split_the_bill
payable_tip_per_person = round(tip_calculation, 2)

print(f"Each person should pay: ${payable_tip_per_person}")