student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

count = 0
total_height = 0


for height in student_heights:
    count +=1
    total_height += height

print(count)
print(total_height)

average = total_height/count

print(round(average))
