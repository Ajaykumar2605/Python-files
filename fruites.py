#Enter how many fruites: 3
#here is your list of fruits
# apple=3
# banana=1
# graps=2
fruits_dic={}
n=int(input("Enter how many fruites: "))
for i in range(n):
    item=input("Enter the fruite you want: ").title() 
    quantity=int(input(f"Enter how many {item} you wants:"))
    fruits_dic[item]= quantity
print("\n here is your list of fruits")
for key,value in fruits_dic.items():
    print(f"{key}={value}")