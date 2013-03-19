import sys, random
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from Tkinter import *

b1 = "up"
xold, yold = None, None
def main():
    root = Tk()
    drawing_area = Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()
def b1down(event):
    global b1
    b1 = "down" # you only want to draw when the button is down
def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None # reset the line when you let go of the button
    yold = None
def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
        xold = event.x
        yold = event.y
if __name__ == "__main__":
    main()