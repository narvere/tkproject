from tkinter import Tk, Entry, Button, RIGHT, END, messagebox, DISABLED, NORMAL

root = Tk()

root.geometry(f"240x270+100+200")
root.resizable(width=False, height=False)
root['bg'] = '#c6e2e9'
root.title("Калькулятор")


def presskey(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '=' or event.char == '\r':
        calculate()


root.bind('<Key>', presskey)


def make_digit(digit):
    """
    Создаетется циферная кнопка
    :param digit: номер кнопки
    :return: экземпляр класса Button
    """
    return Button(root, text=digit, font=("Arial", 13), borderwidth=5, command=lambda: add_digit(digit))


def make_key(key):
    """
    Создаетется операционная кнопка
    :param key: какая операция передается
    :return: экземпляр класса Button
    """
    return Button(root, text=key, borderwidth=5, fg="red", command=lambda: add_operation(key))


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value + operation)
    calc['state'] = DISABLED


def add_digit(digit):
    """
    Вывод вводимых цифр на дисплей
    :param digit: выводимая цифра
    :return: ничего
    """
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value + str(digit))
    calc['state'] = DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc['state'] = NORMAL
    calc.delete(0, END)

    try:
        calc.insert(0, eval(value))
        calc['state'] = DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo(title="Attention!", message="Error!")
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo(title="Attention!", message="No Zero Divison!")
        calc.insert(0, 0)


def clear():
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, "0")
    calc['state'] = DISABLED


def make_calc_button(key):
    return Button(root, text=key, borderwidth=5, fg="red", command=calculate)


def make_clear_button(key):
    return Button(root, text=key, borderwidth=5, fg="red", command=clear)


calc = Entry(root, justify=RIGHT, font=("Arial", 15), width=15)
calc.insert(0, '0')
calc["state"] = DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

make_digit(0).grid(row=4, column=0, sticky="wens", padx=5, pady=5)
make_digit(1).grid(row=1, column=0, sticky="wens", padx=5, pady=5)
make_digit(2).grid(row=1, column=1, sticky="wens", padx=5, pady=5)
make_digit(3).grid(row=1, column=2, sticky="wens", padx=5, pady=5)
make_digit(4).grid(row=2, column=0, sticky="wens", padx=5, pady=5)
make_digit(5).grid(row=2, column=1, sticky="wens", padx=5, pady=5)
make_digit(6).grid(row=2, column=2, sticky="wens", padx=5, pady=5)
make_digit(7).grid(row=3, column=0, sticky="wens", padx=5, pady=5)
make_digit(8).grid(row=3, column=1, sticky="wens", padx=5, pady=5)
make_digit(9).grid(row=3, column=2, sticky="wens", padx=5, pady=5)
make_key("*").grid(row=4, column=3, sticky="wens", padx=5, pady=5)
make_key("+").grid(row=1, column=3, sticky="wens", padx=5, pady=5)
make_key("-").grid(row=2, column=3, sticky="wens", padx=5, pady=5)
make_key("/").grid(row=3, column=3, sticky="wens", padx=5, pady=5)

make_calc_button("=").grid(row=4, column=2, sticky="wens", padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, sticky="wens", padx=5, pady=5)

minsize = 60
root.grid_columnconfigure(0, minsize=minsize)
root.grid_columnconfigure(1, minsize=minsize)
root.grid_columnconfigure(2, minsize=minsize)
root.grid_columnconfigure(3, minsize=minsize)
root.grid_rowconfigure(1, minsize=minsize)
root.grid_rowconfigure(2, minsize=minsize)
root.grid_rowconfigure(3, minsize=minsize)
root.grid_rowconfigure(4, minsize=minsize)

root.mainloop()
