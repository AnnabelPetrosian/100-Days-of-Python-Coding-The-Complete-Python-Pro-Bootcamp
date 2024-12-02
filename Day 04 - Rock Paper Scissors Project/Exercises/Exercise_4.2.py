# Banker Roulette - Who will pay the bill

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#Get the total number of people present in the list
total_number_of_presence = len(names)
# Generate random numbers between 0 and the last index
random_choice = random.randint(0, total_number_of_presence - 1)
# Pick out random person from the list of names using the random numbers
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to pay the bill. ")