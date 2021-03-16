import tkinter as tk;
from login_form import login_form
from register_form import register_form


class main_screen:
    def __init__(self, master):
        self.master = master
        self.main_frame = tk.Frame(self.master)
        # create a Form label 
        self.formlabel=tk.Label(self.main_frame, text="Login Form", bg="blue", width="30", height="2", font=("Calibri", 13)).pack() 
        self.emptyLabel=tk.Label(text="").pack() 
        # create Login Button 
        self.loginButton=tk.Button(self.main_frame,text="Login", height="2", width="30",command=self.new_window_login).pack() 
        self.emptyLabel
        # create a register button
        self.RegisterButton=tk.Button(self.main_frame,text="Register", height="2",width="30",command=self.new_window_register).pack()
        self.emptyLabel
        self.master.protocol("WM_DELETE_WINDOW",self.close)
        self.main_frame.pack()

    def new_window_login(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = login_form(self.newWindow)
        self.master.withdraw()
    
    def new_window_register(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = register_form(self.newWindow)
        self.master.withdraw()

    def close(self):
        self.master.quit()