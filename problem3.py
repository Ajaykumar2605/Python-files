'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3]
         list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
'''
sample_input_list1 = [1,2,3]
sample_input_list2 = [5,6,7]
output_list=[]
if len(sample_input_list1) == len(sample_input_list2):
    for i in range(len(sample_input_list1)):
        sum=sample_input_list1[i]+sample_input_list2[i]
        per=str(sum)
        per.split()
        for j in range(len(per)-1,-1,-1):
           output_list.append(int(per[j]))
print(output_list)



