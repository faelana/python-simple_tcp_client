#!/usr/bin/env python3
import socket

target_host = "google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The AF_INET parameter indicates we’ll use a standard IPv4 address
# or hostname, and SOCK_STREAM indicates that this will be a TCP client.


# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
