import sys
#ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ip="2001:0db8:85a3:0000:0000:8a2e:0370:g334"
#ip=input("Enter the ip address: ")
char_in_ip=['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
new_ip=ip.split(":")
count=0
if len(new_ip)!=8:
    print("Ip is invalid length")
    sys.exit()
for char in ip:
    if char not in char_in_ip:
        print("octet contain invalid character")
        sys.exit()
for i in new_ip:
    if len(i)!= 4:
         print("Ipv6 octaus should have length of 4")
         sys.exit()
for char in ip:
    if char in char_in_ip:
       count+=1
       continue
    else:
       print("Doesn't met the ipv6 requirements")
       sys.exit()
if count!=39:
    print("Ipv6 must contain required octaus")
else:
    print("Ip is valid")