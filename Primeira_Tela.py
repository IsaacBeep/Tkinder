#Comando Abaixo importa tudo da biblioteca que é necessaria
#Para a criação de telas. (Arterisco significa tudo)
from tkinter import *

#i(intaciar = chamar) recebe o objeto Tk(Tkinder)
i = Tk()

#gerar titulo da janela
i.title('Programa financeiro')

#Propriedade que altera o tamanho da janela (980z720) e distancia da direita da tela (250x30)
i.geometry('980x720+950+30')

#Propriedades graficas, cor de fundo da tela (bg) ou (background)
#Não pode passar por i com ponto! DEVE SER I []
i["bg"] = "yellow"

#Cria icone na janela, voce deve ter a imagem no mesmo local do codigo 
#i.wm_iconbitmap('icone.ico')

#Cria um label e posiciona (place). ele em relação na tela.
lb = Label(i, text='Nome do usuario')
lb.place(x=100, y=100)

#Cria um botão que posiciona (place) ele em relação a label.
bt = Button(i, width='20', text='Ok')
bt.place(x=230, y=100) 

#Gera a janela grafica
i.mainloop()