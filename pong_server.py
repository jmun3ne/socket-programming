import socket

def sendPong():
  s=socket.socket() #create socket
  print("Socket succcesfully created")

  # bind server to port
  port = 7000
  s.bind(('',port))

  # start listening to requests
  s.listen(5)
  print("Socket is listening....")

  # pong server running forever
  while True:
    # establish connection with client
    connection, address=s.accept()
    print('Socket connected to ', address)

    # receive message sent by client
    msg =connection.recv(1024).decode()
    print(msg)
    
    # check if message sent is 'ping' or not
    if msg=='ping':
    # respond to the client with Pong if true
     connection.send(str('Pong').encode())
    # close connection with client
     connection.close()
     
    # if message is not 'ping' close the connection of the client
    else:
     connection.close()
# driver function
if __name__ == '__main__':

  # trigger server
  sendPong()
