# BMI calculator
# 1st input: enter height in meters e.g: 1.65
height = input("Please enter your height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Please enter your weight in kilograms: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_float = float(weight)
height_as_float = float(height)

bmi = weight_as_float / height_as_float ** 2
bmi_as_int = int(bmi)
print(f"Your BMI is equal to: {bmi_as_int}")