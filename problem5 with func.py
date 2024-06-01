# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students studying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks in all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
##sorting the list in deascending order
def sort_top(department):
    student_list=[]
    student_list=list(map(int,department))
    student_list.sort(reverse=True)
    return student_list
#avg mark in each department
def avg(department):
    avg=sum(department)/len(department)
    return avg
#find which department is best avg mark
def best_depart(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        best_res='ECE department has best Average'
        return best_res
    elif num2>=num1 and num2>=num3:
        best_res='CSE department has best Average'
        return best_res
    else:
        best_res='EEE department has best Average'
        return best_res
#count failer in overall deparment
def count_fail(department):
    count=0
    for i in range(0,len(department)):
        if department[i]<50:
            count += 1
    return count
#find least failiers in exam 
def least_fail(num1,num2,num3):
    if num1==0 and num2==0 and num3==0:
        least_fail="All passed"
        return least_fail
    elif num1<=num2 and num1<=num3:
        least_fail="ECE"
        return least_fail
    elif num2<=num1 and num2<=num3:
        least_fail="CSE"
        return least_fail
    else:
        least_fail="EEE"
        return least_fail
#find the top 3 in each department
def print_top3(department):
    top_mak=[]
    top_mak.extend(department[0:3])
    return top_mak
#list declaration
ece_student_list=[]
cse_student_list=[]
eee_student_list=[]
#input block
ece_student=input("Enter the mark of ece student: ").split(',')
cse_student=input("Enter the mark of cse student: ").split(',')
eee_student=input("Enter the mark of eee student: ").split(',')
#calling function
ece_student=sort_top(ece_student)
cse_student=sort_top(cse_student)
eee_student=sort_top(eee_student)
#combing three list into single list
total_list=[]
total_list.extend(ece_student)
total_list.extend(cse_student)
total_list.extend(eee_student)
##find the top 3 in each department
print(f"Top 3 mark in ECE:{print_top3(ece_student)}")
print(f"Top 3 mark in CSE:{print_top3(cse_student)}")
print(f"Top 3 mark in EEE:{print_top3(eee_student)}")
#find the top 3 in the over all department
total_list.sort(reverse=True)
print(f"Top 3 marks in over all departmet are:{total_list[0:3]}")
#avg mark in each department
avg_ece=avg(ece_student)
avg_cse=avg(cse_student)
avg_eee=avg(eee_student)
avg_overall=sum(total_list)/len(total_list)
print(f"The average mark of ECE:{round(avg_ece,2)}\nThe average mark of CSE:{round(avg_cse,2)}\nThe average mark of EEE:{round(avg_eee,2)}\n")
#find which department is best avg mark
print(f"{best_depart(avg_ece,avg_cse,avg_eee)}")
#counting fail in departments
ece_fail=count_fail(ece_student)
cse_fail=count_fail(cse_student)
eee_fail=count_fail(eee_student)
#find least failiers in exam 
print(f"The least number of failers in:{least_fail(ece_fail,cse_fail,eee_fail)}")
#result of final exam
print(f"Number of student Attend python Exam:{len(ece_student_list)+len(cse_student_list)+len(eee_student_list)}")
print(f"Total number of failers:{ece_fail+cse_fail+eee_fail}")