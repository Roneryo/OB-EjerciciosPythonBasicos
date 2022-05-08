import tkinter
from pprint import pprint
window = tkinter.Tk()

label_saludo = tkinter.Label(window,text="hola",height=4,width=4,bg="yellow",fg="blue")

label_saludo.pack(ipadx=50,ipady=50,expand=True)



window.mainloop()

# print(type(window))
# pprint(dir(window))