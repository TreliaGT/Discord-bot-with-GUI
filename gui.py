#gui.py
import sys
import tkinter as tk
from tkinter import *
from bot import loadbot 
import threading
import discord 
root = tk.Tk()
root.title('Caller Records For Day') 
root.geometry("1300x600")
root.columnconfigure((0, 2, 3, 4 ,5), weight=1)

class Application(tk.Frame): 
	count = 1
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.grid()
		self.create_widgets()
		
	def addtolist(args , name , phone , message , comapany , Lb1 , c1,c2 ):
		mail = name.get() + ' ' +  comapany.get() + ': ' + phone.get() + ' : ' + message.get()
		Lb1.insert(int(args.count), mail)
		
		args.count = int(args.count) + 1
		name.delete(0, 'end')
		comapany.delete(0, 'end')
		phone.delete(0, 'end')
		message.delete(0, 'end')
		
	def create_widgets(self):
		l1 = tk.Label(self, text = "Name")
		E1 = tk.Entry(self, width=40)
		l1.grid(row = 0, column = 0, pady = 2)
		E1.grid(row = 1, column = 0,  pady = 2)
		l2 = tk.Label(self, text = "Phone")
		E2 = tk.Entry(self , width=40)
		l2.grid(row = 0, column = 1,  pady = 2)
		E2.grid(row = 1, column = 1,  pady = 2)
		l3 = tk.Label(self, text = "Reason")
		E3 = tk.Entry(self, width=80)
		l3.grid(row = 0, column = 3,  pady = 2)
		E3.grid(row = 1, column = 3,  pady = 2)
		l4 = tk.Label(self, text = "Company")
		E4 = tk.Entry(self, width=30)
		l4.grid(row = 0, column = 4,  pady = 2)
		E4.grid(row = 1, column = 4,  pady = 2)
		B = Button(text = "Enter", command = lambda: self.addtolist(E1 , E2 , E3 , E4 , Lb1 , c1,  c2))
		B.grid(row = 0 , column = 5)
		Lb1 = tk.Listbox(self , width=200 , height=30)
		Lb1.grid(row = 3, column=0 , columnspan=5 , pady = 5)
		l5 = tk.Label(self, text = "Discord Notification : Select One")
		l5.grid(row = 2, column = 0,  pady = 2)
		c1 = tk.Checkbutton(self, text='Support',variable='Support', onvalue=1, offvalue=0)
		c1.grid(row = 2 , column = 1)
		c2 = tk.Checkbutton(self, text='Admin',variable='Admin', onvalue=1, offvalue=0)
		c2.grid(row = 2 , column = 2)
		c3 = tk.Checkbutton(self, text='None',variable='None', onvalue=1, offvalue=0)
		c3.grid(row = 2 , column = 3)


class creategui(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self._run()
		
	def _run(self):
		app = Application(master=root)
		app.mainloop()

gui = creategui()
bot = loadbot()
bot.start()
gui.start()



