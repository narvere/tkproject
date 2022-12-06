from tkinter import Tk
from tkinter import Label
from tkinter import BOTTOM, LEFT
from tkinter import Entry, Button, StringVar

root = Tk()

root.title("Kaup24.ee publishing software")
root.geometry("400x200+700+500")
root.resizable(width=True, height=True)

value = StringVar()


def test():
    get = value.get()
    first_text['text'] = get


b = Button(command=test, text="OK")

l = Label(text="Kaup24.ee software")
first_text = Label(text="")
la = Label(text="Author Deniss Hohlov")

e = Entry(textvariable=value)

# b = Button(text="OK")
# b.bind('<Button-1>', test)
# l.grid(row=1, column=1)
# la.grid(row=2, column=1)

l.pack()
e.pack()
b.pack()
first_text.pack(side=LEFT)
la.pack(side=BOTTOM)

# def test():
#     print("test is here")
#
#
# l = Label(text='текст здесь')
# lc = Label(command=test)
# b = Button()
# e = Entry()

root.mainloop()
