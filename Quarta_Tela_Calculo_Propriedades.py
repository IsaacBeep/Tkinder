from tkinter import *

def bt_clickS():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 + num2
        lb["bg"] = "#00FA9A"

    else:
        lb["text"]= "valores sao invalidos"
        lb["bg"]= "red"

def bt_clickSU():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 - num2
        lb["bg"] = "#00FA9A"

    else:
        lb["text"]= "valores sao invalidos"
        lb["bg"]= "red"

def bt_clickM():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 * num2
        lb["bg"] = "#00FA9A"

    else:
        lb["text"]= "valores sao invalidos"
        lb["bg"]= "red"

def bt_clickD():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 / num2
        lb["bg"] = "#00FA9A"

    else:
        lb["text"]= "valores sao invalidos"
        lb["bg"]= "red"


i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb = Label(i, text="0")
lb.place(x=230, y=200)

bt = Button(i, width='20', text='Calcular Soma', bg= 'gray', command=bt_clickS)
bt.place(x=230, y=230)

bt = Button(i, width='20', text='Calcular Subtração', bg= 'pink', command=bt_clickSU)
bt.place(x=230, y=270)

bt = Button(i, width='20', text='Calcular Multiplicação', bg= 'white', command=bt_clickM)
bt.place(x=230, y=310)

bt = Button(i, width='20', text='Calcular Divisão', bg= 'yellow', command=bt_clickD,)
bt.place(x=230, y=350)

lbN = Label(i, bg= 'white',text="IsaacGostoso 😂😂😂😎😎😁😍😍🫥😶‍🌫️😶‍🌫️😭🥶🥵😨😰🤑🤢🥸🥳🥹🤮🤮🤧🤠🤡🤬😡😈👿👽👻☠️💀👺👹👾🤖💩🐵🙊🙈🙈🙉🐯🐶🫁🧒🏿👦🏿")
lbN.place(x=230, y=400)

ed1 = Entry(i)
ed1.place(x=230, y=150)
ed2 = Entry(i)
ed2.place(x=230, y=180)

i.mainloop()