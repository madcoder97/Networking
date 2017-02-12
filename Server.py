from socket import *
host = 'localhost' #"127.0.0.1"
port = 4144
addr = (host,port)
msg = "Hello!"
s=socket(AF_INET,SOCK_DGRAM) 
#s.bind(addr)
s.sendto(msg,addr)
a=1
while a:
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
          a=0
    else:
       a=0
s.close()