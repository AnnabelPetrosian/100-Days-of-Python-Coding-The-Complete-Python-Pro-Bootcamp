## Fix the bugs of code below 👇
#target = int(input())
#for number in range(1, target + 1):
#  if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#  if number % 3 == 0:
#    print("Fizz")
#  if number % 5 == 0:
#    print("Buzz")
#  else:
#    print([number])


# Debugged 👇
target = int(input("Please enter a number between 1-100. \n"))
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:   # use 'and', NOT 'or'
    print("FizzBuzz")
  elif number % 3 == 0:     # use 'elif', NOT 'if'
    print("Fizz")
  elif number % 5 == 0:     # use 'elif', NOT 'if'
    print("Buzz")
  else:
    print(number)           # remove square brackets []