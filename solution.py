from socket import*
import sys
serverPort = 13331
serverSocket = socket (AF_INET, SOCK_STREAM)
print("Socket Created!!")
try:
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The Server is ready to server:',serverPort)

except error as mesg:
print ("Bind Failed. Error Code:"+ str(msg[0]) + "Message:" + msg[1])
sys.exit()

print ('Socket bind complete')
Print ('Socket now listening'
connectionSocket, addr = serverSocket.accept()

print ('source address:' +str(addr))

try:
message = connectionSocket.recv(1024)
print (message, '::',message.split()[0],':',message.split()[1])
filename = message.split()[1]
print (filename, '||',filename[1:])
f = open(filename[1:])
outputdata = f.read()
print (outputdata)
connectionSocket.send('\n HTTP/1.1 200 OK\n\n')
connectionSocket.send(outputdata)
connectionSocket.close()
except IOError:
connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
serverSocket.close()

