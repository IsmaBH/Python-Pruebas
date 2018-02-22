from Tkinter import *

parent = Tk()

z1 = complex
caption = "Numero"

def makeentry(parent, caption, width=10, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "Z1:", 10)
password = makeentry(parent, "Z2:", 10)

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

def callback():
    print content.get()

b = Button(parent, text="get", width=10, command=callback)
b.pack()

mainloop()