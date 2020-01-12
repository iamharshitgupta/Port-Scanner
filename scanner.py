#!/bin/python
import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

else:
	print ("Invalid amount of arguements.")
	print ("Syntax: python3 scanner.py <ip>")

#Add a pretty Banner
print("-" * 50)
print("Scanning Target" +target)
print("Time Started:" +str(datetime.now()))
print("-" * 50)

try:
	for port in range (1,65535):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

#Attempt to connect to a port

result = s.connect_ex((target,port)) #returns an error indicator

if result==0
print("Port {} is open" .format(port))
s.close()

except KeyboardInterrupt:
	print("/n Exiting program.")
	s.close()

except socket.gaierror:
	print("Host name could not be resolved.")
	s.close()


except socket.error:
	print("Couldn't connect to server.")
	s.close()
