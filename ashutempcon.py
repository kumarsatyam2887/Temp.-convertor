from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Tempconv")
root.resizable(0,0)
root.wm_iconbitmap('temp.ico')

# Functions
def convert1():
	label1.config(text= '' +str((var1.get()-32)/1.8)+' C')
	label3.config(text= '' +str((var1.get()-32)/1.8+273)+' k')
	label5.config(text= '' +str((var1.get()-32)*4/9)+' R')

def convert2():
	label2.config(text='' +str(var2.get()*1.8+32)+' F')
	label4.config(text= '' +str((var2.get())+273)+' k')
	label6.config(text= '' +str((var2.get()/5)*4)+' R')

# Variable
var1 = DoubleVar()
var2 = DoubleVar()

# Body Structure
Label(root, text="Temperature Convertor", font="Ds-Digital 35", bg="black", fg="cyan", width=40).pack()

f = Frame(root, bg="black")

Label(f, text="Farenheit", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11).pack(side=LEFT, padx=1)
Label(f, text="Celcius", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11).pack(side=LEFT, padx=1)

f.pack()

f1 = Frame(root, bg="black")

Entry(f1, textvariable=var1, font="Lucida 20", fg="darkblue", justify='center').pack(side=LEFT, padx=90)
Entry(f1, textvariable=var2, font="Lucida 20", fg="darkblue", justify='center').pack(side=LEFT, padx=90)

f1.pack()

f2 = Frame(root, bg="black")

Button(f2, text="Convert", fg="cyan", bg="black", font="Ds-Digital 25", width=28, command=convert1).pack(side=LEFT, pady=11)
Button(f2, text="Convert", fg="cyan", bg="black", font="Ds-Digital 25", width=28, command=convert2).pack(side=LEFT, pady=11)

f2.pack()

f3 = Frame(root, bg="black")

label1 = Label(f3, text="Celcius -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label1.pack(side=LEFT, padx=1)
label2 = Label(f3, text="Farenheit -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label2.pack(side=LEFT, padx=1)

f3.pack()

f4 = Frame(root, bg="black")

label3 = Label(f4, text="Kelvin -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label3.pack(side=LEFT, padx=1)
label4 = Label(f4, text="Kelvin -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label4.pack(side=LEFT, padx=1)

f4.pack()

f5 = Frame(root, bg="black")

label5 = Label(f5, text="Reamur -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label5.pack(side=LEFT, padx=1)
label6 = Label(f5, text="Reamur -:", font="Ds-Digital 25", bg="black", fg="cyan", width=28, pady=11)
label6.pack(side=LEFT, padx=1)

f5.pack()

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()