import sys
import string

ip_address="g001:0db8:85a3:0000:0000:8a2e:0370:g334"
splited_ip=ip_address.split(':')
if len(splited_ip)!=8:
    print("IPv6 does not met eligible cretia")
    sys.exit()
for octa in splited_ip:
    if len(octa)!=4:
         print("Ipv6 octaus should have length of 0 to 4")
         sys.exit()
def valid():
    for ip_char in ip_address:
        if hex(ord(ip_char))!=0x15:
            return False
        else:
            return True
if True:
    print("valid")
elif False:
    print("The string does not contain hex char")
    sys.exit()