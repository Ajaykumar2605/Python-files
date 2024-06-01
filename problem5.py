'''
Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
'''
sample_list=["-","10", "+", "2", "3", "*", "5"]
stack_list=[]
operators=['+','-','*','/']
for i in sample_list:
    if i not in operators:
        stack_list.append(i)
    if i in operators:
        stack_list.append(i)
print(stack_list)