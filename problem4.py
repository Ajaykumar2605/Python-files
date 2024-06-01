'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.

'''
input_list=["1", "2", "+", "5", "*"]
operator =["+","-","*","/","%"]
stack_list=[]
for i in input_list:
    if i not in operator:
       stack_list.append(i)
    if i in operator:
        element1=eval(stack_list.pop())
        if i=='+':
            element2=eval(stack_list.pop())
            result=element1+element2
            stack_list.append(result)
        elif i=='*':
            element2=stack_list.pop()
            result=element1*element2
            stack_list.append(result)
print(stack_list[0])  

