import tkinter as tk;
import chat_screen
import register_form
from functools import partial
import sys
sys.path.append("../")
from server.database.auth import login


class login_form:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #username label and text entry box
        self.usernameLabel = tk.Label(self.frame, text="User Name").grid(row=0, column=0)
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(self.frame, textvariable=self.username).grid(row=0, column=1)  

        #password label and password entry box
        self.passwordLabel = tk.Label(self.frame,text="Password").grid(row=1, column=0)  
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(self.frame, textvariable=self.password, show='*').grid(row=1, column=1)
        self.loginButton = tk.Button(self.frame, text="Login", command=self.new_window_chat).grid(row=4, column=0) 
        self.createAccButton = tk.Button(self.frame,text="Create New Account",command=self.new_window_register).grid(row=4,column=1)
        self.userErrorLabel=tk.Label(self.frame,text="username or password is incorect")
        self.formErrorLabel=tk.Label(self.frame,text="username and password required")
        self.master.protocol("WM_DELETE_WINDOW",self.close)
        self.frame.pack()

    def new_window_chat(self):
        if(self.username.get()=="" or self.password.get()==""):
            self.userErrorLabel.grid_forget()
            self.formErrorLabel.grid(row=5,column=0)
            return
        try:
            if(self.validation()):
                self.newWindow = tk.Toplevel(self.master)
                self.app = chat_screen.chat_screen(self.newWindow,self.username.get())
                self.master.withdraw()
        except:
            self.formErrorLabel.grid_forget()
            self.userErrorLabel.grid(row=5,column=0)
    

    def new_window_register(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = register_form.register_form(self.newWindow)
        self.master.withdraw()
    
    def validation(self):
        return login(self.username.get(),self.password.get())
    
    def close(self):
        self.master.quit()