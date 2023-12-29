# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest = 0
for scores in student_scores:
  if scores > highest:
    highest = scores
print("The highest score in the class is: " + str(highest))

