from socket import *
host = 'localhost' #"255.255.255.255"
port = 12345
addr = (host,port)
msg = "Welcome to the UDP socket chat!"
s=socket(AF_INET,SOCK_DGRAM) 
#s.bind(addr)
s.sendto(msg,addr)
x=0
while x==0:
    try:
        message, address = s.recvfrom(8192) 
        if message:
            print address, "> ", message
    except:
       # print "Error"
        pass
    if message!="bye":
       inpu = raw_input()
       if inpu != False and inpu!="bye":
          s.sendto(inpu, addr)
       elif inpu=="bye":
          s.sendto(inpu, addr)
          x=1
    else:
       x=1
s.close()
