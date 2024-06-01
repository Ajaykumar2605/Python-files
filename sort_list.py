'''
input=[1,2,3,3,3,4,4,7,7,9]
output=[1,2,3,4,7,9,_,_,_,_]

'''
sample_list = [1,2,3,3,3,4,4,7,7,9]
new_list=[]
count=0
for i in sample_list:
    if i not in new_list:
        new_list.append(i)
    else:
        count += 1
new_list.sort()
for space_char in range(count):
    new_list.append('_') 
print(new_list)