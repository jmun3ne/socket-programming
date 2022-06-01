import socket

# function to send ping message
def sendMsg():
  s=socket.socket() #create socket

  # server port to send messages to
  port=7000

  # connect to server on a local machine
  s.connect(('127.0.0.1',port))
  print("Client successfully connected to server")
  
  # prompt user to send message
  msg=input("Enter your message")
  s.send(msg.encode())

  # receive response from server
  msg=s.recv(1024).decode()
  print(message)
  s.close()

# driver function
if __name__ == '__main__':

  # trigger client
  sendMsg()
