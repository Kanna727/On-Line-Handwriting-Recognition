# from flask import Flask
# app=Flask(__name__)
# @app.route("/xyz")

#print('hello world')
#app.run(host="0.0.0.0",debug=True)
# def sample():
#     return 'Hello World'
# app.run(host="192.168.56.1",debug=True, port=8000)

import socket
import sys
 
HOST = '192.168.56.1' #this is your localhost
PORT = 8888
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket: must use to create a socket.
#socket.AF_INET: Address Format, Internet = IP Addresses.
#socket.SOCK_STREAM: two-way, connection-based byte streams.
print('socket created')
 
#Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    #print ('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + str(err[1]))
    sys.exit()
 
print ('Socket Bind Success!')
 
 
#listen(): This method sets up and start TCP listener.
s.listen(10)
print ('Socket is now listening')
 
 
while 1:
    conn, addr = s.accept()
    print ('Connect with ' + addr[0] + ':' + str(addr[1]))
    buf = conn.recv(64)
    print (buf)
s.close()