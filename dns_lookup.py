import socket

ip_info = socket.getaddrinfo("google.com", 0, 
    family=socket.AF_INET, proto=socket.IPPROTO_TCP)

print(ip_info[0][4][0])