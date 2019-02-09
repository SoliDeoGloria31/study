# -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

e = tk.Entry(window, show='*')
e.pack()


def inset_point():
    var = e.get()
    t.insert('insert', var)


def inset_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(
    window,
    text='insert point',
    width=15,
    height=2,
    command=inset_point)
b1.pack()

b2 = tk.Button(
    window,
    text='insert end',
    width=15,
    height=2,
    command=inset_end)
b2.pack()

t = tk.Text(window, height=5)
t.pack()


window.mainloop()
