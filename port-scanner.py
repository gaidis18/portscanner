import socket
import sys
import subprocess
from datetime import datetime

subprocess.call('cls', shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("scanning")

t1 = datetime.now()

try:
    for port in range (x,y):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        print("Scanning Port {}".format(port))
        if (result == 0):
            print ("Port {}:Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You stop the scan.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exitting.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. Exitting.")
    sys.exit()

t2 = datetime.now()

totalTime= t2-t1
print("Scanning Complete in: {}".format(totalTime))
