# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students studying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks in all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
#list declaration
ece_student_list=[]
cse_student_list=[]
eee_student_list=[]
#input block
ece_student=input("Enter the mark of ece student: ").split(',')
cse_student=input("Enter the mark of cse student: ").split(',')
eee_student=input("Enter the mark of eee student: ").split(',')
#sorting the list in deascending order
ece_student_list=list(map(int,ece_student))
ece_student_list.sort(reverse=True)
cse_student_list=list(map(int,cse_student))
cse_student_list.sort(reverse=True)
eee_student_list=list(map(int,eee_student))
eee_student_list.sort(reverse=True)
#combing three list into single list
total_list=[]
total_list.extend(ece_student_list)
total_list.extend(cse_student_list)
total_list.extend(eee_student_list)
#find the top 3 in each department
print(f"Top 3 mark in ECE:{ece_student_list[0:3]}")
print(f"Top 3 mark in CSE:{cse_student_list[0:3]}")
print(f"Top 3 mark in EEE:{eee_student_list[0:3]}")
#find the top 3 in the over all department
total_list.sort(reverse=True)
print(f"Top 3 marks in over all departmet are:{total_list[0:3]}")
#avg mark in each department
avg_ece=sum(ece_student_list)/len(ece_student_list)
avg_cse=sum(cse_student_list)/len(cse_student_list)
avg_eee=sum(eee_student_list)/len(eee_student_list)
avg_overall=sum(total_list)/len(total_list)
print(f"The average mark of ECE:{round(avg_ece,2)}\nThe average mark of CSE:{round(avg_cse,2)}\nThe average mark of EEE:{round(avg_eee,2)}\n")
#find which department is best avg mark
if avg_ece>=avg_cse and avg_ece>=avg_eee:
    print('ECE department has best Average')
elif avg_cse>=avg_ece and avg_cse>=avg_eee:
    print('CSE department has best Average')
else:
    print('EEE department has best Average')
#counting fail in departments
fail_ece=0
fail_cse=0
fail_eee=0
for i in range(0,len(ece_student_list)):
    if ece_student_list[i]<50:
        fail_ece += 1
for i in range(0,len(cse_student_list)):
    if cse_student_list[i]<50:
        fail_cse += 1
for i in range(0,len(eee_student_list)):
    if eee_student_list[i]<50:
        fail_eee += 1
#find least failiers in exam 
if fail_ece==0 and fail_cse==0 and fail_eee==0:
    least_fail="All passed"
elif fail_ece<=fail_cse and fail_ece<=fail_eee:
    least_fail="ECE"
elif fail_ece<=fail_cse and fail_ece<=fail_eee:
    least_fail="CSE"
else:
    least_fail="EEE"
#result of final exam
print(f"Number of student Attend python Exam:{len(ece_student_list)+len(cse_student_list)+len(eee_student_list)}")
print(f"Total number of failers:{fail_ece+fail_cse+fail_eee}")
print(f"The least number of failers in:{least_fail}")
##output
# Enter the mark of ece student: 90,80,67,50
# Enter the mark of cse student: 89,98,76,40
# Enter the mark of eee student:  50,89,100,60
# Top 3 mark in ECE:[90, 80, 67]
# Top 3 mark in CSE:[98, 89, 76]
# Top 3 mark in EEE:[100, 89, 60]
# Top 3 marks in over all departmet are:[100, 98, 90]
# The average mark of ECE:71.75
# The average mark of CSE:75.75
# The average mark of EEE:74.75
# CSE department has best Average
# Number of student Attend python Exam:12
# Total number of failers:1
# The least number of failers in:ECE