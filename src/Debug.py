import tkinter as tk
from tkinter import ttk
import socket

class ClientGUI:
    #public 
    a = None
    m_Window = None #window	
    m_Title = "Chat Client"
    m_Size = "300x400"
    m_Frame = None #Frame
    m_SendButton = None #Button 
    m_TextArea = None #TextArea / ListBox
    m_TextField = None
    m_ClientSocket = None
    m_nickname = None
    m_address = None
    m_port = None
    
    def __init__(self,nickname,address,port):
        self.m_Window = tk.Tk()
        self.m_Window.geometry(self.m_Size)
        self.m_Window.title(self.m_Title)
        self.m_Window.resizable(False, False)
        self.m_Frame = tk.Frame(self.m_Window)
        self.m_TextArea = tk.Listbox(self.m_Frame, height=20, width=50)
        self.m_TextField = tk.Text(self.m_Window,height=2, width=25)
        self.m_SendButton = ttk.Button(self.m_Window, text="send", command=self.onBtnClick)
        self.m_Frame.pack()
        self.m_TextArea.pack(side=tk.LEFT, fill=tk.BOTH)
        self.m_TextField.pack(side=tk.LEFT)
        self.m_SendButton.pack(side=tk.RIGHT)
        try:
            self.m_ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.m_ClientSocket.connect((socket.gethostname(), 1111))
        except Exception:
            print ("Error while Connecting to Server")
        print("Connected to Server ")
        self.m_ClientSocket.sendall(bytes("/c/First Connection","utf-8"))
        
    def send(self,msg):
        self.m_ClientSocket.sendall(bytes("/m/" + msg,"utf-8"))
    
    def receive(self):
        data = self.m_ClientSocket.recv(1024)
    
    def update(self):
        self.m_Window.mainloop()
        self.m_ClientSocket.close()
        
    def onBtnClick(self, event = None):
        textfieldmsg = self.m_TextField.get('1.0', "end-1c") 
        self.m_TextArea.insert(tk.END, textfieldmsg)
        self.send(textfieldmsg)
        self.m_TextField.delete('1.0', 'end-1c') #clears

#clientGUI = ClientGUI("spil3141","localhost","1111")
#clientGUI.update()