import socket
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.56.1', 8888)) #IP is the server IP
 
for args in sys.argv:
    if args == "":
        args = 'no args'
    else:
        s.sendall(args.encode('utf-8'))
 
print ('goodbye!')