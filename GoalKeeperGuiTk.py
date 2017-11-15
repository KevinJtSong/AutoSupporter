from tkinter import *
from tkinter import scrolledtext
from GoalKeeper_v0_4_1 import *
import threading
#GUI
root = Tk()
root.title("GoalKeeper")

Label(root, font=('Open Sans',10), text="SIMS ID").grid(row=0, padx = 10, pady = 1)
Label(root, font=('Open Sans',10), text="Password").grid(row=1, padx = 10, pady = 1)
Label(root, font=('Open Sans',10), text="ServiceNow URL").grid(row=2, padx = 10, pady = 1)
Label(root, font=('Open Sans',10), text="Time").grid(row=3, padx = 10, pady = 1)
console = scrolledtext.ScrolledText(root, font=('Open Sans',10),fg='white',bg='black')

console.grid(row = 0, column=2, rowspan = 5, pady = 5)

x = StringVar()
y = StringVar()
z = StringVar()
n = StringVar()

e1 = Entry(root, font=('Open Sans',10), textvariable = x)
e2 = Entry(root, font=('Open Sans',10), textvariable = y)
e3 = Entry(root, font=('Open Sans',10), textvariable = z)
e4 = Entry(root, font=('Open Sans',10), textvariable = n)

x.set("KEVISONG")
y.set("Schenker160503!10")
z.set("https://schenkeritsmprod.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_clear_stack%3Dtrue%26sysparm_query%3DGOTOnumber%253DINC000497402%26sysparm_fixed_query%3D'")
n.set("1")

e1.grid(row=0, column=1, padx = 10, pady = 1)
e2.grid(row=1, column=1, padx = 10, pady = 1)
e3.grid(row=2, column=1, padx = 10, pady = 1)
e4.grid(row=3, column=1, padx = 10, pady = 1)



button = Button(root,text = "Go",command = lambda:run(e1.get(),e2.get(),e3.get(),e4.get()))
button.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = W + E + N + S)


mainloop()

