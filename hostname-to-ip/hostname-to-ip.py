# import socket module
import socket

# get hostname
hostname=input("Input hostname: ")

# get ip of hostname
ip=socket.gethostbyname(hostname)
print(ip)
