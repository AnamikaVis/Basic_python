student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for height in student_heights:
  sum_height += height
total_number = 0
for number in student_heights:
  total_number += 1
average_height = round(sum_height/total_number)
print("total height = " + str(sum_height))
print("number of students = " + str(total_number))
print("average height = " + str(average_height))

