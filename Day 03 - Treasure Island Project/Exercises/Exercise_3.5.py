print("The Love Calculator is calculating your love score ... ")
name1 = input("What is your name? ")
name2 = input("What is your partner's name? ")

# Write your code below this line 👇

combined_names = name1 + name2
lower_case_names = combined_names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
first_digit = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if (love_score < 10) or (love_score > 90):
    print(f"Your Love score is {love_score}, you go together like coke and mentos. ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your Love score is {love_score}, you are alright together.")
else:
    print(f"Your Love score is {love_score}.")
