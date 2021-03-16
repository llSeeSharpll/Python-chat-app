import tkinter as tk;
import login_form
from functools import partial
import sys
sys.path.append("../")
from server.database.auth import register

class register_form:
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
        

        #email label and text entry box
        self.emailLabel = tk.Label(self.frame, text="Email").grid(row=2, column=0)
        self.email = tk.StringVar()
        self.emailEntry = tk.Entry(self.frame, textvariable=self.email).grid(row=2, column=1)

        #email label and text entry box
        self.mobileLabel = tk.Label(self.frame, text="Mobile Number").grid(row=3, column=0)
        self.mobile = tk.StringVar()
        self.mobileEntry = tk.Entry(self.frame, textvariable=self.mobile).grid(row=3, column=1)

        self.RegisterButton = tk.Button(self.frame, text="Register", command=self.new_window_register).grid(row=4, column=0) 
        self.loginButton = tk.Button(self.frame,text = "Have an Account?",command=self.new_window_login).grid(row=4,column=1)
        self.errorLabel=tk.Label(self.frame,text="Username already taken")
        self.formErrorLabel= tk.Label(self.frame,text="Please fill all the enteries in form")
        self.master.protocol("WM_DELETE_WINDOW",self.close)
        self.frame.pack()

    def new_window_register(self):
        if(self.username.get()=="" or self.password.get()=="" or self.email.get()=="" or self.mobile.get()==""):
            self.errorLabel.grid_forget()
            self.formErrorLabel.grid(row=5,column=0)
            return 
        try:
            if(self.validation()):
                self.newWindow = tk.Toplevel(self.master)
                self.app = login_form.login_form(self.newWindow)
                self.master.withdraw()
        except:
            self.formErrorLabel.grid_forget()
            self.errorLabel.grid(row=5,column=0)

    

    def new_window_login(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = login_form.login_form(self.newWindow)
        self.master.withdraw()
            
    
    def validation(self):
        return register(self.username.get(),self.password.get(),self.mobile.get(),self.email.get())
    
    def close(self):
        self.master.quit()