import socket
import datetime
from os.path import exists
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
s.connect((host,port))
print s.recv(1024).center(50," ")
if exists("clientchat.txt"):
	filerd=open("clientchat.txt",'r')
	print filerd.read()
file=open("clientchat.txt",'a')
print (s.recv(2)+"<").rjust(50," ")
file.write("hi<".rjust(50," "))
file.write("\n")
while True:
	dt=raw_input(">")
	if dt=="xexitx":
		s.send(dt)
		break
	else:
		s.send(dt)
		file.write(">"+dt+"\n")
		temp=s.recv(1024)
		if temp=="xexitx":
			print "Connection closed by server.".center(50," ")
		else:
			print (temp+"<").rjust(50," ")
			file.write((temp+"<").rjust(50," "))
			file.write("\n")
s.close()
now=str(datetime.datetime.now())
file.write("\n\n\n")
file.write(now.center(50," "))
file.write("\n\n\n")
file.close()
