
from tkinter import *
from math import *


def avancer():
    global angle, x, y, xp, yp
    angle += 15
    xp, yp = x, y
    x = x_center - cos(radians(angle))*echelle
    y = y_center - sin(radians(angle))*echelle
    can.coords(oval, x-15, y-15, x+15, y+15)
    can.create_line(xp, yp, x, y, fill='blue')
    can.create_line(x_center, y_center, x, y, fill='yellow')


def reculer():
    global angle, x, y, xp, yp
    angle -= 15
    xp, yp = x, y
    x = x_center - cos(radians(angle))*echelle
    y = y_center - sin(radians(angle))*echelle
    can.coords(oval, x-15, y-15, x+15, y+15)
    

echelle, x_center, y_center, angle, x, y = 100, 200, 200, 0, 100, 200

fen = Tk()
can = Canvas(fen, width=400, height=400, bg='black')
can.grid(row=0, column=0)
oval = can.create_oval(x-15, y-15, x+15, y+15, fill='white')
bou_a = Button(fen, text='Avancer', command=avancer)
bou_a.grid(row=1, sticky=W)
bou_r = Button(fen, text='Reculer', command=reculer)
bou_r.grid(row=1, sticky=E)

fen.mainloop()
