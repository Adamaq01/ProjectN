import socket

PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", PORT))

s.send("Bonjour :)")

s.close()
