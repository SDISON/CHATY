import socket
from os.path import exists
import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(2)
#server=s.getsockname()
c,addr=s.accept()
#client1=s.getpeername()
client1="client1"
print "successfully connected to client".center(50," ")
c.send("successfully connected to server")
print "\n\n\n"
if exists("serverchat.txt"):
	filerd=open("serverchat.txt",'r')
	print filerd.read()	
file=open("serverchat.txt",'a')
c.send("hi")
file.write(">hi\n")
while True:
	temp=c.recv(1024)
	if temp=="xexitx":
		print "Connection break by client.".center(50," ")
	else:
		print (temp+"<").rjust(50," ")
		file.write((temp+"<").rjust(50," "))
		file.write("\n")
	dt=raw_input(">")
	if dt=="xexitx":
		c.send(dt)
		break
	else:
		c.send(dt)
		file.write((">"+dt)+"\n")	
c.close()
s.close()
now=str(datetime.datetime.now())
file.write("\n\n\n")
file.write(now.center(50," "))
file.write("\n\n\n")	
file.close()
