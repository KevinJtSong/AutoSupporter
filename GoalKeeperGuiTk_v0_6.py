from tkinter import *
from tkinter import scrolledtext
from GoalKeeper_v0_6 import *
import threading
#GUI


root = Tk()
root.title("GoalKeeper")

Label(root, font=('Open Sans',10), text="SIMS ID").grid(row=0, padx = 10, sticky=W)
Label(root, font=('Open Sans',10), text="Password").grid(row=1, padx = 10, sticky=W)
Label(root, font=('Open Sans',10), text="ServiceNow URL").grid(row=2, padx = 10, sticky=W)
Label(root, font=('Open Sans',10), text="Time").grid(row=3, padx = 10,sticky=W)


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

e1.grid(row=0, column=1, padx = 20)
e2.grid(row=1, column=1, padx = 20)
e3.grid(row=2, column=1, padx = 20)
e4.grid(row=3, column=1, padx = 20)


button_start = Button(root,text = "Start", font=('Open Sans',10),command = lambda:run_multi(e1.get(),e2.get(),e3.get(),e4.get()))
#button_stop = Button(root, text = "Stop", font=('Open Sans',10),command = stop_multi)
button_start.grid(row = 9, column = 0, rowspan = 6, columnspan = 2, padx = 10, pady = 10, sticky = W + E + N + S)
#button_stop.grid(row = 12, column = 0, rowspan = 3, columnspan = 2, padx = 10, pady = 10, sticky = W + E + N + S)

console = scrolledtext.ScrolledText(root, font=('Open Sans',10),fg='white',bg='black')

console.grid(row = 0, column=2, rowspan = 15, pady = 10)

if __name__=='__main__':
	mainloop()

