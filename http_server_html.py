from socket import *
serverSocket = socket (AF_INET, SOCK STREAM)

serverSocket.bind(('192.168.100.130',8088))
serverSocket.listen(1)
print ('Ready to serve...')
connectionSocket, addr = serverSocket.accept()
try:
	message = connectionSocket.recv(1024)
	print (message. decode())
	print (message.split0)[1]. decode())
	filename = message,split()[1]
	f = open(filename[l:])
	outoutdata = f.read()
	f.close()

	connectionSocket.send('HTTP/1.0 200 oK\r\n\r\n'.encode())
	for i in range(0, len(outputdata)):
		connectionsocket.send(outputdata[i].encode())
	connectionSocket.close()
except IOError:
	connectionSocket.send(404 Not Found'.encode())
	connectionSocket.close()
serverSocket close()
