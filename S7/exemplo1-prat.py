from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()

photo = PhotoImage(file='computer.gif')#.subsample(5)

image = Label(master=root, image=photo)

text = Label(master=root, font=("Arial", 36), text='Este é um TESTE!')

image.pack(side=TOP, fill='x',)

text.pack(side=BOTTOM)

root.mainloop()