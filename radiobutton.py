from tkinter import Tk, Radiobutton, Label, IntVar, StringVar

win = Tk()
win.geometry("400x400+150+150")
win.title("Tere maailm")

level_var = IntVar()
second_level_var = IntVar()
level_text = StringVar()

Label(win, text="Radiobuttons list").pack()

first = 'Fist radiobutton'
second = "Second radiobutton"
third = "Third radiobutton"


def select_level():
    level = level_var.get()
    level_text.set(f"Вы выбрали {level}")
    if level == 1:
        print(first)
    elif level == 2:
        print(second)
    elif level == 3:
        print(third)


Label(win, text="Мой первый блок")
Radiobutton(win, text=first, variable=level_var, value=1, command=select_level).pack()
Radiobutton(win, text=second, variable=level_var, value=2, command=select_level).pack()
Radiobutton(win, text=third, variable=level_var, value=3, command=select_level).pack()
Label(win, textvariable=level_text).pack()
Label(win, text="Мой второй блок")
Radiobutton(win, text="Эльфы", variable=second_level_var, value=1, command=select_level).pack()
Radiobutton(win, text="Орки", variable=second_level_var, value=2, command=select_level).pack()
Radiobutton(win, text="Люди", variable=second_level_var, value=3, command=select_level).pack()
""
win.mainloop()
