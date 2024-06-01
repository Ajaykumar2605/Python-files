import re
ip_add=input("Enter the ip address: ")
#pattern=
if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",ip_add):
#pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.',ip_add)
#print(pattern)
#if pattern==True:
    print("your ip is valid")
else:
    print("your ip is invalid")
