from Tkinter import *

caption = ""
parent = Tk()
z1 = complex(0,0)

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

def callback():
    print text

#content = StringVar()
#entry = Entry(parent, text=caption, textvariable=content)

#text = content.get()
#content.set(text)
content = StringVar()
user = makeentry(parent, "User name:", 10, textvariable=content)
password = makeentry(parent, "Password:", 10)

text = content.get()
content.set(text)
b = Button(parent, text="get", width=5, command=callback)
b.pack()

mainloop()