from Tkinter import *
from math import *

def evaluate(event):
	res.configure(text="calculadora: " + str(eval(entry.get())))

w = Tk()
Label(w, text="Expresion: ").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()