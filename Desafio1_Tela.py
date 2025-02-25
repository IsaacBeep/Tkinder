from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')
i["bg"] = "#b5b5b5"

lb1 = Label(i, text="Login", bg= "#51AFF7")
lb1.place(x= 1200, y=120 ) #Componente .grid serve tambem para posicionar utilizando indicativo que linha(row) e coluna(column) 

lb2 = Label(i, text="Senha", bg="white")
lb2.place(x= 1200, y=140)

ed1 = Entry(i)
ed1.place(x= 1250, y=120)
ed2 = Entry(i)
ed2.place(x= 1250, y=140)

bt1 = Button(i, text="Login", width=10)
bt1.place(x=920, y=480)

i.mainloop()