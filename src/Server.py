import socket 
import threading
class Server:

    m_Socket = None
    m_Clients = list()
    m_ClientAddress = None
    m_ConnectionThread = None
    m_ListeningThread = None
    m_running = False
    
    def __init__(self,address,port):
        self.m_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(self.m_Socket == None):
            print("Error Connecting")
            return
        print("Connection started on port : " + str(port))
        self.m_Socket.bind((address,port))
        self.m_Socket.listen(5)
        self.m_ConnectionThread = threading.Thread(target = self.listenForNewConnection,name= "Listening for new client Thread")
        self.m_ConnectionThread.start()
#        self.m_ListeningThread = threading.Thread(target = self.listenforClient,name= "Listening for client Thread")
        

    def listenForNewConnection(self):
        while(not self.m_running):
            client, address = self.m_Socket.accept()
            nickname = client.recv(1024).decode("utf-8")[3:]
            print("New Connection made with: " + str(address) + " -" + nickname  + "-")
            self.registerClients(nickname,client,address)
            print("Number of Clients: " + str(len(self.m_Clients)))
            try:
                pass
            except Exception:
                print("Error in -listenForNewConnection-")
    
    def registerClients(self,nickname,client,address):
        self.m_Clients.append([nickname,client,address])
        client.sendall(bytes("Connected to server as: " + nickname,"utf-8"))
        tempThread = threading.Thread(target=self.listen,args = (client,nickname,), name = nickname)
        tempThread.start()
        print(nickname + " listening thread started")
#        self.m_ListeningThread.start() #start listening on client sockets
        
        
    def listen(self, client,nickname):
        while(not self.m_running):
            msg = client.recv(1024)
            self.processReceivedMsg(msg,nickname)
        
    def processReceivedMsg(self,msg,nickname):
        if (msg.decode("utf-8")[:3] == "/m/"):
            for i in self.m_Clients:
                i[1].sendall(bytes(nickname +  ": " +  msg.decode("utf-8")[3:],"utf-8"))
                print("send msg to : " + i[0]  )
        else:
            print("-Messgae from client has strange format-")
        
    
    def exit(self):
        self.m_running = True
#        self.m_Socket.close()
#        if(self.m_ConnectionThread.isAlive()):
#            self.m_ConnectionThread.join()
#        if(self.m_ListeningThread.isAlive()):
#            self.m_ListeningThread.join()
#        print("Thread is Alive: " + str(self.m_ConnectionThread.isAlive()))
        print("Server Shutdown: True")
    
if __name__ == "__main__":
    address = input("Enter the address: ")
    port = input("Enter the port: ")
    if(address != "" and port != ""):
        port = int(port)
        if(port >=0):
            server = Server(address,port)
            input("Enter to exit")
            server.exit()




#    def listenforClient(self):
#        while(not self.m_running):
#            try:
#                for i in self.m_Clients:
#                    tempThread = threading.Thread(target=self.listen,args = (i[1],), name = i[0])
#                    tempThread.start()
#                    print(i[0] + " listening thread started")
##                    msg = i[1].recv(1024)
##                    print(str(i[0]) + ": " + msg.decode("utf-8"))
##                    self.processReceivedMsg(msg)
#            except:
#                print("Error in listenforClient")
                