#create a text file to stored in ipv6 address
#access the file from the program in write mode
#check wether the given string is ipv6 or not 
#get the input from the text file 
#text file each line containts ipv6 verify all the ip's and print valid or not
#***************************************************************************** 


def validation(address):
    address=address.replace('\n','')
    splited_ip=address.split(':')   
    if len(splited_ip)!=8:
        result="IPv6 does not met eligible criteria"
        return result
    for octet in splited_ip:
        if not (len(octet)>0 and len(octet)<=4):
           result="The length of octaus is must be 4"
           return result
    count=0   
    for octuas in splited_ip:
        try:
            int(octuas,16)
        except ValueError:
            count += 1
    if count==0:
        result="IP address is valid"  
        return result      
    else:
        result="the given string is does not contain hex value"
        return result
       
   
f = open(f'file.txt','r')
n=0
for line in f:
   n += 1
   print(f"\nLINE NO {n} :{validation(line)}")
   continue
f.close()




