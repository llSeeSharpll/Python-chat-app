#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
import main_screen

class chat_screen:
    def __init__(self, master,username):
        self.master = master
        self.messages_frame = tk.Frame(self.master)
        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("Type your messages here.")
        self.scrollbar = tk.Scrollbar(self.messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tk.Listbox(self.messages_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()





        self.entery_frame = tk.Frame(self.master)
        self.entry_field = tk.Entry(self.entery_frame, textvariable=self.my_msg,)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack(side="left")
        self.send_button = tk.Button(self.entery_frame, text="Send", command=self.send)
        self.send_button.pack(side="right")
        self.entery_frame.pack()
        self.back_button = tk.Button(self.master,text="Back",command=self.back)
        self.back_button.pack()





        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        #----Now comes the sockets part----
        self.HOST = '192.168.78.1'
        self.PORT = '33000'
        if not self.PORT:
            self.PORT = 33000
        else:
            self.PORT = int(self.PORT)

        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.username=username

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.my_msg.set(self.username)
        self.send()
        self.my_msg.set("enter text here")
        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()
    
    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
                self.msg_list.insert(tk.END, msg)
            except OSError:  # Possibly client has left the chat.
                break


    def send(self,event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            self.master.quit()

    def back(self):
        self.my_msg.set("{quit}")
        msg = self.my_msg.get()
        self.client_socket.send(bytes(msg, "utf8"))
        self.newWindow = tk.Toplevel(self.master)
        self.app = main_screen.main_screen(self.newWindow)
        self.master.withdraw()

    def on_closing(self,event=None):
        """This function is to be called when the window is closed."""
        self.my_msg.set("{quit}")
        self.send()
