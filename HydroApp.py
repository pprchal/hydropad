from tkinter import *
import tkinter as tk
from project.engines.osc import OSCEngine
from project.engines.midi import MIDIEngine
from config import config
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
        butt = tk.Button(self, command=self.quitClick, text='Quit', bg='green')
        butt.pack()

    def callback(self, url):
        webbrowser.open_new(url)
    
    def open_qr_img(self):
        url = f'http://{config.server_name()}:{config.server_port()}'
        link1 = Label(self.master, text='Open web browser - hydropad', fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: self.callback(url))        

        code_xbm = printQR(config.server_name(), config.server_port())
        code_bmp = tk.BitmapImage(master=self.master, data=code_xbm)
        panel = tk.Label(image = code_bmp)
        panel.image = code_bmp
        panel.pack()
        

    def quitClick(self):
        self.webServer.shutdown()
        self.quit()


def createGUI():
    root = tk.Tk()
    root.title("hydropad 0.2")
    root.geometry('800x800')
    app = HydroApp(master=root)
    return app

def create_engine():
    if config.engine() == "OSC":
        return OSCEngine()
    else:
        return MIDIEngine()

# engine = create_engine()
server = HydroServer()
server.start()

app = createGUI()
app.mainloop()





