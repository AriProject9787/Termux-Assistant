import os
import subprocess as sp
ip=input("Enter your ip:")
port=int(input("Enter your port:"))
path=input("Enter a file path with file name:")
location=input("Enter a location:")
a=int(input("Enter your option:1 for copy 2 for paste:"))
if(a==1):
    sp.call("scp -P {} {}:{} {} ".format(port,ip,path,location),shell=True)
elif(a==2):
    sp.call("scp -P {} {} {}:{}".format(port,path,ip,location),shell=True)
else:
    print("Enter a correct option")