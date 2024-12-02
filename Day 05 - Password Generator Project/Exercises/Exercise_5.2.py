# High Score
# Input a list of student scores
student_scores = input("Enter student scores. \n").split()
for n in range(0, len(student_scores)):
    student_scores[0] = int(student_scores[n])

# Write your code below this row 👇

hightes_score = 0
for score in student_scores:
    if score > hightes_score:
        hightes_score = score


print(f"The hightes score in the class is: {hightes_score}")