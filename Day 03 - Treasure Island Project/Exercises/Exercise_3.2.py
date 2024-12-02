# BMI 2.0

# Enter your height in meters e.g., 1.55
height = float(input("Please enter your height in meters. "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Please enter your weight in kilograms. "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_calculation = weight / height ** 2

if bmi_calculation < 18.5:
    print(f"Your BMI is {bmi_calculation}, you are underweight !!!")
elif bmi_calculation >= 18.5 and bmi_calculation < 25:
    print(f"Your BMI is {bmi_calculation}, you have a normal weight.")
elif bmi_calculation >= 25 and bmi_calculation < 30:
    print(f"Your BMI is {bmi_calculation}, you are slightly overweight.")
elif bmi_calculation >= 30 and bmi_calculation < 35:
    print(f"Your BMI is {bmi_calculation}, you are obese.")
elif bmi_calculation >= 35:
    print(f"Your BMI is {bmi_calculation}, you are clinically obese !!!")
else:
    print("The input data is wrong. Please try again. ")