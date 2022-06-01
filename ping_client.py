import socket

# function to send ping request
def sendMessage():
  s=socket.socket() #create socket

  # server port to send messages to
  port = 7000

  # connect to server on a local machine
  s.connect(('127.0.0.1',port))
  print("Client successfully connected to server:")
  
  # prompt user to send message
  message =input("Enter your message")
  s.send(message.encode())

  # receive response from server
  message=s.recv(1024).decode()
  print(message)
  s.close()

# driver function
if __name__ == '__main__':

  # trigger client
  sendMessage()
