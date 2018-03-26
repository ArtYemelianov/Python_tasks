#!/usr/bin/python3.6
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", 9999))

message = input("Enter message that is going to be sent on server ")

s.send(message.encode())
data = s.recv(1024)
print("Received", data)
s.close()
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # bind the socket to a public host, and a well-known port
# serversocket.bind((socket.gethostname(), 9999))
# # become a server socket
# serversocket.listen(5)
#
#
# while True:
#     # accept connections from outside
#     (clientsocket, address) = serversocket.accept()
#     # now do something with the clientsocket
#     # in this case, we'll pretend this is a threaded server
#     ct = client_thread(clientsocket)
#     ct.run()
