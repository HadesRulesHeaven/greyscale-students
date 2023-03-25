import socket
serverip='172.17.29.11'
serverport=6000
serveraddress=(serverip,serverport)
bufferSize=1024
clientsocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
message="Hola mi nombre es Ritvik"
bytestosend=str.encode(message)
clientsocket.sendto(bytestosend,serveraddress)
