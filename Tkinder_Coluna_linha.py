from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text="Login", bg= "pink")
lb1.place(x= 1700) #Componente .grid serve tambem para posicionar utilizando indicativo que linha(row) e coluna(column) 

lb2 = Label(i, text="Senha", bg="red")
lb2.place(x= 1700, y=)

ed1 = Entry(i)
ed1.place(x= 1750)
ed2 = Entry(i)
ed2.grid(row=2, column=2)

bt1 = Button(i, text="Login")
bt1.grid(row=4, column=2)


i.mainloop()