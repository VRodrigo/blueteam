#%%
#! /usr/bin/env python
import socket
import os
from scapy.all import *

# -----------------Socket creation-----------------

buffer = ""

ip_info = socket.gethostbyname('8.8.8.8')

proto = socket.getprotobyname("ICMP")

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto)

sock.setsockopt((socket.SOL_SOCKET, socket.SO_RCVBUF, buffer))

#print(ip_info)

# ----------------send packages---------------------



sock.close()

# %%
