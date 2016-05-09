#Author: Andrew Clavin
#Saturday, May 7th, 2016
'''
Create a main program that displays a menu to the user.
The first item should be to select an appropriate image to be manipulated.
The last item on the list is to exit the program.
In between, you will need menu items that will
(a) create a grayscale of the image selected in the first menu item,
(b) create a warmer version of the image selected in the first menu item,
(c) create a cooler version  of the image selected in the first menu item,
(d) create a brighter/less bright version of the image selected
in the first menu item,
(e) create a negative version  of the image selected in the first menu item,
(f) and finally one function of your own making that is not described
anywhere in the text.
'''
import tkinter as tk
import tkinter.filedialog
from tkinter import *
import image as img
import sys

master = Tk()
closers = []
def upload():
    '''Function uploads an image'''
    newFile = filedialog.askopenfile(parent=master,mode='rb',title='Choose a file')
    global photo
    photo = img.Image(file = newFile.name, title = 'Test')
    photo.show()

def manipulateImage(image, title, change):
    print (image)
    '''Prepares image for manipulaton'''
    width = image.width()
    height = image.height()
    newPhoto = img.Image(width, height, title = title)
    for y in range(height):
        for x in range(width):
            color = image.get(x, y)
            newPhoto.set(x, y, change(color))
    closers.append(newPhoto)
    return newPhoto

def makeBitsGreyscale(pix):
    '''Turns a pixel grey'''
    brightness = (pix[0] + pix[1] + pix[2]) // 3
    return (brightness, brightness, brightness)

def makeBitsWarmer(pix):
    '''Increase R and a little G channels'''
    r = pix[0] + ((255 - pix[0]) // 10)
    g = pix[1] + ((255 - pix[1]) // 20)
    return (r, g, pix[2])

def makeBitsCooler(pix):
    '''Increases B and a little G channels'''
    b = pix[2] + ((255 - pix[2]) // 10)
    g = pix[1] + ((255 - pix[1]) // 20)
    return (pix[0], g, b)

def tintBits(pix):
    '''Brightens pixel'''
    return( pix[0] + ((255 - pix[0]) // 10), pix[1] + ((255 - pix[1]) // 10), pix[2] + ((255 - pix[2]) // 10))


def shadeBits(pix):
    '''Darkens pixel'''
    return( pix[0] - (pix[0] // 5), pix[1] - (pix[1] // 5), pix[2] - (pix[2] // 5))

def invertBits(pix):
    '''Darkens pixel'''
    return( 255 - pix[0], 255 - pix[1], 255 - pix[2])

def rotateBits(pix):
    '''Switches the channels around'''
    return(pix[1], pix[2], pix[2])

def desaturate(image, title):
    return manipulateImage(image, title, makeBitsGreyscale)

def warm(image, title):
    return manipulateImage(image, title, makeBitsWarmer)

def cool(image, title):
    return manipulateImage(image, title, makeBitsCooler)

def tint(image, title):
    return manipulateImage(image, title, tintBits)

def shade(image, title):
    return manipulateImage(image, title, shadeBits)

def invert(image, title):
    return manipulateImage(image, title, invertBits)

def rotate(image, title):
    return manipulateImage(image, title, rotateBits)

def close():
    master.destroy()
    photo._quitWhenAllDone()
    for pic in closers:
        pic._quitWhenAllDone()
    sys.exit()
    
def main():    
    browse = Button(master, text='Browse', command=upload)
    desaturateB = Button(master, text="Desaturate", command= lambda: desaturate(photo, "Dest Image").show())
    warmB = Button(master, text="Warm", command= lambda: warm(photo, "Warm Image").show())
    coolB = Button(master, text="Cool", command= lambda: cool(photo, "Cool Image").show())
    tintB = Button(master, text="Tint", command= lambda: tint(photo, "Tinted Image").show())
    shadeB = Button(master, text="Shade", command= lambda: shade(photo, "Shaded Image").show())
    invertB = Button(master, text="Invert", command= lambda: invert(photo, "Inverted Image").show())
    musicalChairB = Button(master, text="Wacky", command= lambda: rotate(photo, "Musical Chaired Image").show())
    closeB = Button(master, text="Close", command=close)
    browse.pack()
    desaturateB.pack()
    warmB.pack()
    coolB.pack()
    tintB.pack()
    shadeB.pack()
    invertB.pack()
    musicalChairB.pack()
    closeB.pack()
    mainloop()

main()
    

