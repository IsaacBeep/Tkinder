from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')
i["bg"] = "#b5b5b5"

""" lb3 = Label(i, text="")
lb3.grid(row=0, column=0)

lb4 = Label(i, text="")
lb4.grid(row=1, column=0)

lb1 = Label(i, text="LOGIN", bg= "yellow")
lb1.grid(row=1, column=1)

lb5 = Label(i, text="")
lb5.grid(row=2, column=0)

lb2 = Label(i, text="SENHA", bg="red")
lb2.grid(row=3, column=1)

ed1 = Entry(i)
ed1.grid(row=1, column=2)

ed2 = Entry(i)
ed2.grid(row=3, column=2)

bt1 = Button(i, text="OK", width=10)
bt1.grid(row=4, column=2)
 """

lb3 = Label(i, text="", width=5, height=3)
lb3.grid(row=0, column=0)

lb4 = Label(i, text="")
lb4.grid(row=1, column=0)

lb1 = Label(i, text="LOGIN", bg= "yellow")
lb1.grid(row=1, column=1)

lb5 = Label(i, text="")
lb5.grid(row=2, column=0)

lb2 = Label(i, text="SENHA", bg="red")
lb2.grid(row=3, column=1)

ed1 = Entry(i)
ed1.grid(row=1, column=2)

ed2 = Entry(i)
ed2.grid(row=3, column=2)

bt1 = Button(i, text="OK", width=10)
bt1.grid(row=4, column=2)

i.mainloop()