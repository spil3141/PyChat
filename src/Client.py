#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 16, 2019 03:10:18 PM JST  platform: Windows NT

import sys
import tkinter as tk
from tkinter import ttk
import socket
import threading



class Toplevel1:
    
    m_Window = None
    m_Nickname = ""
    m_Address = ""
    m_Port = 0
    
    m_ClientSocket = None
    m_ListenThread = None
    
    
    
    def __init__(self):
        
        #WINDOW CREATION
        self.m_Window = tk.Tk()
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font14 = "-family 휴먼엑스포 -size 14 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font15 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font9)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.m_Window.geometry("361x508+673+145")
        self.m_Window.minsize(120, 1)
        self.m_Window.maxsize(1905, 1170)
        self.m_Window.resizable(1, 1)
        self.m_Window.title("Calendar")
        self.m_Window.configure(background="wheat")
        self.m_Window.configure(highlightbackground="wheat")
        self.m_Window.configure(highlightcolor="black")

        #FRAME 1        
        self.Frame2 = tk.Frame(self.m_Window)
        self.Frame2.place(relx = 0.0, rely = 0.0, relheight = 1.014, relwidth = 1.011)
        self.Frame2.configure(relief = 'groove')
        self.Frame2.configure(borderwidth = "2")
        self.Frame2.configure(relief = "groove")
        self.Frame2.configure(background = "#ffffff")
        
        #FRAME 2 ELEMENTS
        self.Listbox1 = tk.Listbox(self.Frame2)
        self.Listbox1.place(relx = 0.0, rely = 0.0, relheight = 0.835, relwidth = 0.971)
        self.Listbox1.configure(background = "white")
        self.Listbox1.configure(disabledforeground = "#a3a3a3")
        self.Listbox1.configure(font = "TkFixedFont")
        self.Listbox1.configure(foreground = "#000000")
        
        self.Text2 = tk.Text(self.Frame2)
        self.Text2.place(relx = 0.0, rely = 0.874, relheight = 0.066, relwidth = 0.704)
        self.Text2.configure(background = "white")
        self.Text2.configure(font = "TkTextFont")
        self.Text2.configure(foreground = "black")
        self.Text2.configure(highlightbackground = "wheat")
        self.Text2.configure(highlightcolor = "black")
        self.Text2.configure(insertbackground = "black")
        self.Text2.configure(selectbackground = "#c4c4c4")
        self.Text2.configure(selectforeground = "black")
        self.Text2.configure(wrap = "word")
        
        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx = 0.747, rely = 0.874, height = 34, width = 67)
        self.Button2.configure(activebackground = "#f4bcb2")
        self.Button2.configure(activeforeground = "#000000")
        self.Button2.configure(background = "wheat")
        self.Button2.configure(command = self.onSentBtnClick)
        self.Button2.configure(disabledforeground = "#a3a3a3")
        self.Button2.configure(foreground = "#000000")
        self.Button2.configure(highlightbackground = "wheat")
        self.Button2.configure(highlightcolor = "black")
        self.Button2.configure(pady = "0")
        self.Button2.configure(text = '''Send''')
        
        #FRAME 2
        self.Frame1 = tk.Frame(self.m_Window)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.011)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")
        self.Frame1.configure(cursor="fleur")

        #FRAME 2 ELEMENTS
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.356, rely=0.777, height=51, width=97)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="wheat")
        self.Button1.configure(command=self.onBtnClick)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.247, rely=0.214, relheight=0.058, relwidth=0.477)

        self.Text1.configure(background="white")
        self.Text1.configure(font=font15)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="wheat")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Text1_2 = tk.Text(self.Frame1)
        self.Text1_2.place(relx=0.247, rely=0.563, relheight=0.058
                , relwidth=0.477)
        self.Text1_2.configure(background="white")
        self.Text1_2.configure(font="-family {DejaVu Sans} -size 14")
        self.Text1_2.configure(foreground="black")
        self.Text1_2.configure(highlightbackground="wheat")
        self.Text1_2.configure(highlightcolor="black")
        self.Text1_2.configure(insertbackground="black")
        self.Text1_2.configure(selectbackground="#c4c4c4")
        self.Text1_2.configure(selectforeground="black")
        self.Text1_2.configure(wrap="word")

        self.Text1_3 = tk.Text(self.Frame1)
        self.Text1_3.place(relx=0.247, rely=0.388, relheight=0.058
                , relwidth=0.477)
        self.Text1_3.configure(background="white")
        self.Text1_3.configure(font="-family {DejaVu Sans} -size 14")
        self.Text1_3.configure(foreground="black")
        self.Text1_3.configure(highlightbackground="wheat")
        self.Text1_3.configure(highlightcolor="black")
        self.Text1_3.configure(insertbackground="black")
        self.Text1_3.configure(selectbackground="#c4c4c4")
        self.Text1_3.configure(selectforeground="black")
        self.Text1_3.configure(wrap="word")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.356, rely=0.155, height=25, width=104)
        self.TLabel1.configure(background="#000000")
        self.TLabel1.configure(foreground="#a6a6a6")
        self.TLabel1.configure(font=font14)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Nickname''')

        self.TLabel1_4 = ttk.Label(self.Frame1)
        self.TLabel1_4.place(relx=0.329, rely=0.33, height=25, width=120)
        self.TLabel1_4.configure(background="#000000")
        self.TLabel1_4.configure(foreground="#a6a6a6")
        self.TLabel1_4.configure(font="-family {휴먼엑스포} -size 14")
        self.TLabel1_4.configure(relief="flat")
        self.TLabel1_4.configure(text='''IP Address''')

        self.TLabel1_5 = ttk.Label(self.Frame1)
        self.TLabel1_5.place(relx=0.411, rely=0.505, height=25, width=104)
        self.TLabel1_5.configure(background="#000000")
        self.TLabel1_5.configure(foreground="#a6a6a6")
        self.TLabel1_5.configure(font="-family {휴먼엑스포} -size 14")
        self.TLabel1_5.configure(relief="flat")
        self.TLabel1_5.configure(text='''Port''')
        
        #Starting socket listen thread
        self.m_ListenThread = threading.Thread(target=self.listen)
       
    def connectSocket(self,nickname,address,port):
        #SOCKET SETUP 
        try:
            self.m_ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.m_ClientSocket.connect((address, port))
        except Exception:
            print ("Error while Connecting to Server")
        print("Connected to Server ")
        self.m_ClientSocket.sendall(bytes("/c/" + nickname,"utf-8"))
    
    def listen(self):
        while(True):
            # print(self.m_ListenThread.isAlive())
            msg_from_server = self.m_ClientSocket.recv(1024).decode("utf-8")
            self.console(msg_from_server)
                
    def console(self,msg):
        self.Listbox1.insert(tk.END, msg)
        
    def send(self,msg):
        self.m_ClientSocket.sendall(bytes("/m/" + msg,"utf-8"))
        
    def switchFrames(self):
        self.Frame1.destroy()
        
    def onSentBtnClick(self,event = None):
        textfieldmsg = self.Text2.get('1.0', "end-1c") 
        # self.Listbox1.insert(tk.END, textfieldmsg)
        self.send(textfieldmsg)
        self.Text2.delete('1.0', 'end-1c') #clears
        
    def onBtnClick(self,event = None):
        self.m_Nickname = self.Text1.get('1.0', "end-1c")
        self.m_Address = self.Text1_3.get('1.0', "end-1c")
        self.m_Port = int(self.Text1_2.get('1.0', "end-1c"))
        self.Text1.delete('1.0', 'end-1c')
        self.Text1_2.delete('1.0', 'end-1c')
        self.Text1_3.delete('1.0', 'end-1c')
        self.switchFrames()
        self.connectSocket(self.m_Nickname,self.m_Address,self.m_Port)
        self.m_ListenThread.start()
    
    def update(self):
        self.m_Window.mainloop()
        self.m_ClientSocket.close()
        
        
        
if __name__ == "__main__":
    client = Toplevel1()
    client.update()
