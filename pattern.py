ip=input("enter the ip: ")
list_ip=[]
count=0
list_ip=ip.split('.')  
if len(list_ip)==4 :
    if int(list_ip[0])<=255 and int(list_ip[1])<=255 and int(list_ip[2])<=255 and int(list_ip[3])<=255:
            print("valid")
    else:
        print("invalid")
else:
    print("invalid")