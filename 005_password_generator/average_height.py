student_heights = input("Input a list of heights in cms separated by space: ").split()
# size = len(student_heights)
# sum = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  # sum += student_heights[n]

# print(f"total height = {sum}")
# print(f"number of students = {size}")
# print(f"average height = {round(sum / size)}")

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in number_of_students:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")