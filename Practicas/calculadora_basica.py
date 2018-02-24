#Importaciones necesarias...
from tkinter import *
#import tkinter.messagebox
import matplotlib.pyplot as plt

#Definimos el metodo para graficar las respuestas
def move_spines():
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax
#Metodo para calcular la suma
def Suma():
   n1=complex(caja1.get())
   n2=complex(caja2.get())
   suma=n1+n2
   print (suma)
   """ax = move_spines()
   ax.set_xlim(-100, 100)
   ax.set_ylim(-100, 100)
   ax.grid()
   ax.scatter(suma.real, suma.imag)"""
   #tkinter.messagebox.showinfo("Mensaje","El resultado es: %f + j%f"%suma.real + suma.imag)
   caja1.delete(0,20)
   caja2.delete(0,20)

#Metodo para calcular la resta
def Resta():
   n1=complex(caja1.get())
   n2=complex(caja2.get())
   resta=n1-n2
   print (resta)
   #tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
   caja1.delete(0,20)
   caja2.delete(0,20)

#Metodo para calcular la multiplicacion
def Multiplicacion():
   n1=complex(caja1.get())
   n2=complex(caja2.get())
   multiplicacion=n1*n2
   print (multiplicacion)
   #tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
   caja1.delete(0,20)
   caja2.delete(0,20)

#Metodo para calcular la division
def Division():
   n1=complex(caja1.get())
   n2=complex(caja2.get())
   division=n1/n2
   print (division)
   #tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
   caja1.delete(0,20)
   caja2.delete(0,20)
#Creacion del GUI
gui = Tk()
#Titulo del GUI
gui.title("MiniCalculadora")
#Dimensiones (ancho,alto,posicion x,posicion y)
gui.geometry("400x250+400+200")

#Creacion de una etiqueta
var1 = StringVar()
var1.set("Escribe el primer numero:")
label1 = Label(gui,textvariable=var1,height = 2)
label1.pack()

#Creacion de una caja de texto para el primer numero
numero1=StringVar()
caja1=Entry(gui,bd=4,textvariable=numero1)
caja1.pack()

#Creacion de otra etiqueta
var2 = StringVar()
var2.set("Escribe el segundo numero:")
label2 = Label(gui,textvariable=var2,height = 2)
label2.pack()

#Creacion de otra caja de texto para el segundo numero
numero2=StringVar()
caja2=Entry(gui,bd=4,textvariable=numero2)
caja2.pack()

#Boton para la suma
boton1 = Button(gui, text = "Suma", command = Suma,width=15)
boton1.pack()

#Boton para la resta
boton2 = Button(gui, text = "Resta", command = Resta,width=15)
boton2.pack()

#Boton para multiplicacion
boton3 = Button(gui, text = "Multiplicacion", command = Multiplicacion,width=15)
boton3.pack()

#Boton para la division
boton4 = Button(gui, text = "Division", command = Division,width=15)
boton4.pack()

#Cargar el GUI
gui.mainloop()