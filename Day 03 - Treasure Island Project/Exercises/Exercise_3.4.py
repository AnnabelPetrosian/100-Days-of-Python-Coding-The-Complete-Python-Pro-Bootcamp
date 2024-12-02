print("Thank you for choosing Python Pizza Deliveries. ")
pizza_size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0
if pizza_size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif pizza_size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif pizza_size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("Wrong input, try again!!! ")

if extra_cheese == "Y":
    bill += 1

print(f"Thank you for ordering. Your final bill is ${bill}.")