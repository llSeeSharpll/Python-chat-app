import tkinter as tk
from main_screen import main_screen 



def main(): 
    root = tk.Tk()
    root.title("Chat App")
    root.geometry("300x300")
    app = main_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()