from random import randint
from tkinter import Label
from tkinter import Tk

root = Tk()


def testimine():
    x = randint(1, 10)
    print(x)


def new_label():
    x = randint(1, 10)
    label = Label(root, text=x)
    label.pack()
