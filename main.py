import socket
import sys
import re
from datetime import datetime
import os

#Funtions----------------------------------------------------------------------------------------------

def banner(target):
    print("_" * 50 + "\n")
    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))
    print("_" * 50 + "\n")

def ip_selection(target):
    banner(target)
    try:
    #scan every port on the target ip
        for port in range(1,100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            #return open port
            result = s.connect_ex((target,port))
            if(result == 0):
                print(port,end=" ")
                print("[*] port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting ...")
        sys.exit()
    except socket.error:
        print("\n Host is not exits ...")
        sys.exit()
    

def url_selection(target):
    target = socket.gethostbyname(target)
    ip_selection(target)


#Enterence ---------------------------------------------------------------------------------------------
os.system('cls')
print("Port scanner started ...")

ctrl = int(input("IP(1)/URL(2)\n>> "))
loopctrl = True

try:
    while loopctrl:
        if ctrl == 1:
            print("ip query")
            os.system('cls')
            target = str(input("Target IP:\n>>> "))
            ip_selection(target)
            loopctrl = False
        elif ctrl == 2:
            os.system('cls')
            target = str(input("Target URL:\n>>> "))
            url_selection(target)
            loopctrl = False
        else:
            os.system('cls')
            print("You did not choose 1 or 2 ...") 
            ctrl = int(input("IP(1)/URL(2)\n>> "))
except socket.gaierror:
    print("Target is not exits")
    sys.exit()

print("\n")