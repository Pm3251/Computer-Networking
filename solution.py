# import socket module
from socket import *
# In order to terminate the program


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(('', port))
  serverSocket.listen(1)
  print('The server is ready to server:', port)

  while True:
    connectionSocket, addr = serverSocket.accept()

    try:
      try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        response = 'HTTP/1.1 200 OK \r\n\r\n'
        connectionSocket.send(response.encode())
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())
          print ('Got the page:', filename)
        connectionSocket.close()

      except IOError:
        print ('IOError')
        Didnotfind = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(Didnotfind.encode())
        print ('404 NOT FOUND THE PAGE')
        outputdata = '404 NOT FOUND THE PAGE'
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
      except (ConnectionResetError, BrokenPipeError):
        pass

  serverSocket.close()
  sys.exit()
if __name__ == "__main__":
  webServer(13331)
