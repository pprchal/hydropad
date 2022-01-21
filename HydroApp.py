from tkinter import *
import tkinter as tk
from project.Runtime import Runtime
from project.Config import Config
from project.gui.qr import printQR
from project.http.HydroServer import HydroServer
import webbrowser

class HydroApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.open_qr_img()
        butt = tk.Button(self, command=self.on_quit_click, text='Quit', bg='green')
        butt.pack()

    def callback(self, url):
        webbrowser.open_new(url)
    
    def open_qr_img(self):
        url = f'http://{Config.server_name()}:{Config.server_port()}/'
        link1 = Label(self.master, text='Open web browser - hydropad', fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: self.callback(url))        

        code_xbm = printQR(Config.server_name(), Config.server_port())
        code_bmp = tk.BitmapImage(master=self.master, data=code_xbm)
        panel = tk.Label(image = code_bmp)
        panel.image = code_bmp
        panel.pack()
        
    def on_quit_click(self):
        Runtime.server.quit()
        self.quit()

def create_gui():
    root = tk.Tk()
    root.title("hydropad 0.4 +websock")
    root.geometry('800x800')
    app = HydroApp(master=root)
    return app

Runtime.init()
Runtime.server = HydroServer()            
Runtime.server.start()


# create_gui().mainloop()

print("<ENTER>")
input()





