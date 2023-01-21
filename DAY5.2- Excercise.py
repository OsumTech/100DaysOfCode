student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# final_number = student_scores[0]

# for numbers in student_scores:
    
#     if numbers > final_number:
#         final_number = numbers
#         greater_number = numbers
#     else:
#         greater_number = final_number 

greater_number = 0

for number in student_scores:
    if number > greater_number:
        greater_number = number

print(greater_number)
