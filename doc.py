from tkinter import *
import time

xplacity = 3
yplacity = 5  # the speed of the y
width = 500
height = 500
window = Tk()

canvas = Canvas(window, width=width, height=height)
canvas.pack()

bk = PhotoImage(file='bk.png')
pic = PhotoImage(file='her.png')
bkimage = canvas.create_image(0, 0, image=bk, anchor=NW)
myimage = canvas.create_image(0, 0, image=pic, anchor=NW)
image_xplacity = pic.width()
image_yplacity = pic.height()
while True:
    # to get the coords of the image according into the canvas
    cordinates = canvas.coords(myimage)
    print(cordinates)

    if cordinates[0] > (width-image_xplacity) or cordinates[0] < 0:
        xplacity = -xplacity
    if cordinates[1] > (width-image_yplacity) or cordinates[1] < 0:
        yplacity = -yplacity
    canvas.move(myimage, xplacity, yplacity)
    window.update()
    time.sleep(0.01)
window.mainloop()
