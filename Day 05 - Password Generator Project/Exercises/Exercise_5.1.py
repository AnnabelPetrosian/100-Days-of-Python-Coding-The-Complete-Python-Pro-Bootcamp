# Average Height
# Input a Python list of student heights
student_heights = input("Input students height. \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


#print(student_heights)

# 🚨 Don't change the code above 👆

# Write your code below this row 👇

#number_of_students = len(student_heights)
sum_of_heights = 0
for height in student_heights:
  sum_of_heights += height
print(f"Sum of sutudent's hetight is equal to {sum_of_heights}. ")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"Number of students is equal to {number_of_students}.")

average_height = round(sum_of_heights / number_of_students)

print(f"The average height of students is equal to {average_height}. ")