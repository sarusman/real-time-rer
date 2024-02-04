import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import os, datetime
from api import api


window=tk.Tk()
w=1350
h=800
window.title('TIME REAL')
window.geometry(str(w)+"x"+str(h))
window.configure(bg='#FFFFFF')


class f:
	def __init__(self):
		self.Label_middle = tk.Label(window, text ="")
		self.h = tk.Label(window, text ="HEURE : "+datetime.datetime.now().strftime('%H : %M'))


	def update(self):
		self.hour()
		self.horaire()
		window.after(10000, self.update)

	def horaire(self):
		data=api.get_horaire("", "", 0)
		print(data)
		self.h = tk.Label(window, text =data[0], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.43)

		self.h = tk.Label(window, text =data[1], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.67)

		self.h = tk.Label(window, text =data[2], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.9)

		data=api.get_horaire("", "", 1)
		self.h = tk.Label(window, text =data[0], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.31)

		self.h = tk.Label(window, text =data[1], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.55)

		self.h = tk.Label(window, text =data[2], fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.67, rely = 0.78)


	def hour(self):
		self.h = tk.Label(window, text =datetime.datetime.now().strftime('%H:%M'), fg="gold")
		self.h.config(font=("Courier", 59))
		self.h.place(relx = 0.70, rely = 0.07)
		
	def kill(self):
		self.Label_middle.destroy()
		self.h.destroy()



gtr=f()

def ligne_rer():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "235", 0))


def ligne_366():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "366", "Solferino"))

def ligne_140():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "140", "Solferino"))




def ligne_13():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("metro", "13", "asnieres+gennevilliers+les+courtilles"))



image = Image.open(os.getcwd()+"/images/lignes/HEAD.png")
resize_image = image.resize((w, h))

ligne_rer_logo = ImageTk.PhotoImage(resize_image)

#ligne_140_logo = PhotoImage(file = os.getcwd()+"/images/lignes/607.png")
#ligne_13_logo = PhotoImage(file = os.getcwd()+"/images/lignes/620.png")
#ligne_366_logo = PhotoImage(file = os.getcwd()+"/images/lignes/366.png")

Button(window, image = ligne_rer_logo, command=ligne_rer).place(x=0, y=0)
#Button(window, image = ligne_140_logo, command=ligne_140).place(x=420, y=100)
#Button(window, image = ligne_13_logo, command=ligne_13).place(x=670, y=100)
#Button(window, image = ligne_366_logo, command=ligne_366).place(x=820, y=100)



gtr.update()

window.mainloop()
