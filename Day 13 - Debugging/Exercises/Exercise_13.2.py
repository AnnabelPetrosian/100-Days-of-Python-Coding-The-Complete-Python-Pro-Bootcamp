## Fix the bugs of code below 👇
#number = int(input()) # Which number do you want to check?
#
#if number % 2 = 0:
#  print("This is an even number.")
#else:
#  print("This is an odd number.")
  

# Debugged 👇
number = int(input("Which number do you want to check? ")) # Which number do you want to check?

# if number % 2 = 0: -> This is a bug / an Error
# Remember that single '=' is assignment.
# Double '==' is checking for equality. 
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  