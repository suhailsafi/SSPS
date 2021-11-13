#Importing libraries.
import socket
import sys
import os
import shutil
from datetime import datetime


#Clearing screen
os.system("cls" if os.name == "nt" else "clear")


#Printing welcome massage.
welcome_text = """
 ____ ____  ____  ____
/ ___/ ___||  _ \/ ___|
\___ \___ \| |_) \___ \
 ___) ___) |  __/ ___) |
|____|____/|_|   |____/

"""

columns = shutil.get_terminal_size().columns
print(welcome_text.center(columns))
print("\n Coded by suhail safi at 2021.")


#Changing the domain name to ipv4 to scan it, if it's.
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invaild amount of argument. enter a valid target")

#Scaning the target massage.
print("*" * 50)
print("Scanning target: " + target)
print("scanning started at: " + str(datetime.now()))
print("-" * 50)

#Trying to connect to the vailed 1000 ports of the target.
try:
        for port in range(1,1000):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.6)

                result = s.connect_ex((target,port))
                if result ==0:
                        print("Port {} has been located as opened.".format(port))
                s.close()
        

#Closing the scanner if there's a keyboard interrupt.
except KeyboardInterrupt:
        print("\n Closing scanner.")
        sys.exit()

#Closing the scanner if the target can't be reached
except socket.gaierror:
	print("\n The target can't be reached, try scanning it later.")
	sys.exit()


#Closing the scanner if the library server can't be reached.
except socket.error:
        print("\ Server is not responding.")
        sys.exit()
#end
