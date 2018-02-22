from Tkinter import *
#from Tkinter import messagebox


def multiply(var1, var2, var3):
    product = var1 * var2 * var3
    messagebox.showinfo(str(product))
    return product


def btnClick(event):
    x = float(entry.get())



main = Tk()
main.title("Assignment 16")

main.geometry("500x500")
main["bg"] = "#000066"

lblFirst = Label(main, text="Amount to Pay: ")
lblFirst.grid(row=0, column=3, pady=5)

amount = " "
amount.set("default")
entry = Entry(main, width=20)
entry.grid(row=0, column=4)

lblSecond = Label(main, text="Interest Rate (like 7.5): ")
lblSecond.grid(row=2, column=3, pady=10)

rate = " "
rate.set("default")
entry2 = Entry(textvariable=rate)
entry2.grid(row=2, column=4)

lblThird = Label(main, text="Years to Pay: ")
lblThird.grid(row=4, column=3, pady=15)

years = " "
years.set("default")
entry3 = Entry(textvariable=years)
entry3.grid(row=4, column=4)

num3 = int(years)

lblFourth = Label(main, text="Monthly Payment: ")
lblFourth.grid(row=6, column=3, pady=15)
lblFourthTwo = Label(main, text="XXXXX")
lblFourthTwo.grid(row=6, column=4)
lblFifth = Label(main, text="Total of Paymenta: ")
lblFifth.grid(row=8, column=3, pady=15)
lblFifthTwo = Label(main, text="XXXXX")
lblFifthTwo.grid(row=8, column=4)

button1 = Button(main, text="Convert", width=10, command=btnClick)
button2 = Button(main, text="Calculate", width=10, command=multiply(amount, rate, years))
button1.grid(padx=20, pady=20)
messagebox(amount, rate, years)
main.mainloop()