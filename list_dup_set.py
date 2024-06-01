'''
input=[1,2,3,3,3,4,4,7,7,9]
output=[1,2,3,4,7,9,_,_,_,_]

'''
sample_list = [1,2,3,3,3,4,4,7,7,9]
output_list=[]
output_list=list(set(sample_list))
count=len(sample_list)-len(output_list)
for i in range(count):
  output_list.append('_')
print(output_list)