ece_marks_list=[]
ece_marks=input("Enter the mark of ECE students: ").split(',')
# cse_marks=input("Enter the mark of CSE students: ").split(',')
# eee_marks=input("Enter the mark of EEE students: ").split(',')
#sort the marks of student in ascending order
ece_marks=list(map(int,ece_marks))
ece_marks.sort()
# cse_marks=cse_marks.sort()
# eee_marks=eee_marks.sort()
print(ece_marks)
# print(cse_marks)
# print(eee_marks)
