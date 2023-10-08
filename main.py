from tkinter import *

'''
the first line of code Tk() this allows us to open a graphical interface
otherwise the program closes 
'''
open_program = Tk()

def read_file():
    #print (e1_soft.get())
    value = float(e1_soft.get()) * 1.6
    t1.insert(END, value)


b1 = Button(open_program, text="Execute",command = read_file )
#b1.pack() " this is one way to execute a button
b1.grid(row = 0, column = 0) #gives us more control

e1_soft = StringVar()

e1 = Entry(open_program, textvariable=e1_soft)
e1.grid(row=0, column = 1)

t1 = Text(open_program, height =2, width=23)
t1.grid(row=0, column= 2)


open_program.mainloop()