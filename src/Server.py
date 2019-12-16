import socket 
import threading

class Server:

    m_Socket = None
    m_Client = None
    m_ClientAddress = None
    m_ListenThread = None

    def __init__(self,address,port):
        self.m_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(self.m_Socket == None):
            print("Error Connecting")
            return
        print("Connection started on port : 1111")
        self.m_Socket.bind((address,port))
        self.m_Socket.listen(5)
        self.listen()

    def listen(self):
        while(True):
            self.m_Client, self.m_CLientAddress = self.m_Socket.accept()
            self.processReceivedMsg(self.m_Client.recv(1024))
#            self.m_Client.sendall(b"got it")

    def processReceivedMsg(self,msg):
        print(msg.decode("utf-8"))
    
if __name__ == "__main__":
    address = input("Enter the address: ")
    port = input("Enter the port: ")
    if(address != "" and port != ""):
        port = int(port)
        if(port >=0):
            server = Server(address,port)
            server.m_Socket.close()



