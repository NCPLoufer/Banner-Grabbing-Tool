#!/usr/bin/python3

import socket

s = socket.socket()
s.settimeout(5)

ip = input('Enter the ip address: ')
port = str(input('Enter the port: '))

s.connect((ip, int(port)))

print(s.recv(1024).strip('b'))
