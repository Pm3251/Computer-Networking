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
        connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n")
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")
        connectionSocket.close()

      except IOError:
        print ('IOError')
        connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n")
        connectionSocket.close()
    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()

if __name__ == "__main__":
  webServer(13331)