# Leap Year

# Which year do you want to check
year = int(input("Please enter the year you would like to cheack. "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year. ")
        else:
            print("Not Leap year. ")
    else:
        print("Leap year. ")
else:
    print("Not Leap year. ")
