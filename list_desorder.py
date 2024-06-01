'''
input=[1,2,3,3,3,4,4,7,7,9]
output=[1,2,3,4,7,9,_,_,_,_]

'''
sample_list = [1,2,3,3,3,4,4,7,7,9]
new_list=[]
count=0
prev_element=''
for i in sample_list:
    if prev_element!=i:
        new_list.insert(0,i)
    else:
        count += 1
    prev_element=i
#new_list.sort()
for space_char in range(count):
    new_list.append('_') 
print(new_list)