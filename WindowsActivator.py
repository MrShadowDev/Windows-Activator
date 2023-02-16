import tkinter as tk
import os

class WindowsActivator:
    def __init__(self, master):
        self.master = master
        self.master.title('Windows 10/11 activator')
        self.master.configure(bg='#133C55')
        
        self.font = ("Helvetica", 24)
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Windows Activator by MrShadowDev", font=self.font, bg='#133C55', fg='#EBEBEB').grid(column=1, row=0)
        home_button = tk.Button(self.master, text="Home", font=("Helvetica", 16), bg='#59A5D8', fg='#EBEBEB', command=lambda: self.activate_windows('home'))
        pro_button = tk.Button(self.master, text="Pro", font=("Helvetica", 16), bg='#59A5D8', fg='#EBEBEB', command=lambda: self.activate_windows('pro'))

        home_button.grid(column=1, row=1)
        pro_button.grid(column=1, row=2)

    def activate_windows(self, option):
        if option == 'home':
            os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
            os.system("slmgr /skms s8.uk.to")
            os.system("slmgr /ato")
        elif option == 'pro':
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            os.system("slmgr /skms s8.uk.to")
            os.system("slmgr /ato")
    
    def run(self):
        self.master.mainloop()

if __name__ == '__main__':
    app = WindowsActivator(tk.Tk())
    app.run()
