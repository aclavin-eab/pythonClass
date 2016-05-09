import tkinter as tk
import tkinter.filedialog
from tkinter import *
import imageEditor

master = Tk()
test = "hey"
file = ""
myImage = ""

def callback():
    print (test)
def askopenfile():
    file = filedialog.askopenfile(parent=master,mode='rb',title='Choose a file')
    '''if file != None:
        data = file.read()
        file.close()
        print ("done")'''
    print (file)
    myImage = imageEditor(file.name)
def desaturate():
    print (file)
    myImage.desaturate("desatImage")
    #desatImg.show()

browse = Button(master, text='Browse', command=askopenfile)
desaturate = Button(master, text="Desaturate", command=desaturate)
warm = Button(master, text="Warm", command=callback)
cool = Button(master, text="Cool", command=callback)
tint = Button(master, text="Tint", command=callback)
shade = Button(master, text="Shade", command=callback)
close = Button(master, text="Close", command=callback)
browse.pack()
desaturate.pack()
warm.pack()
cool.pack()
tint.pack()
shade.pack()
close.pack()

mainloop()
