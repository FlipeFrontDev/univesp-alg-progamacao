# passo 1: importar bibliotecas e classes de janela

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk() #Passo 2: Objeto da classe de criação de telas

photo = PhotoImage(file='computer.gif').subsample(5) # Escala imagem 1:5px

image = Label(master=root, image=photo)

image.pack(side=TOP)

text = Label(master=root, font=("Courier", 18), text='Olá alunos da UNIVESP!')

text.pack(side=BOTTOM)

#hello = Label(master=root, image=photo, width=300, height=180) #Passo 3: objeto com parametros - master: local de inserção da label
#hello.pack() #Empacotamento dos elementos criados na janela

root.mainloop() #Implementa a janela na tela