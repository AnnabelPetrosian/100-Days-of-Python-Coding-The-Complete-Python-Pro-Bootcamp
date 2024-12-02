# Adding Even Numbers
target = int(input("Enter a number between 0 and 1000. ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

sum_of_even_numbers = 0
for even_number in range(0, target + 1, 2):
#    print(even_number)
    sum_of_even_numbers += even_number

print(sum_of_even_numbers)


# Or


sum_of_even_numbers = 0
for even_number in range(2, target + 1, 2):
#    print(even_number)
    sum_of_even_numbers += even_number

print(sum_of_even_numbers)


# Or


alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number

print(alternative_sum)


