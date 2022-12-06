from var import *
from tkinter import Tk
from random import randint
from tkinter import PhotoImage
from tkinter import Label, Button, Entry
from tkinter import RAISED, LEFT, RIGHT, DISABLED, NORMAL, END

root = Tk()
photo = PhotoImage(file=favico)
root.iconphoto(False, photo)

root.title(title)

root.config(bg=bg_color)
root.geometry(window_geometry)
# root.minsize(width=30, height=30)
root.resizable(width=False, height=False)

lb = Label(root, text=lb_text, bg=lb_txt_bg_color, fg=lb_txt_color, font=(lb_font, lb_font_size, lb_font_type),
           padx=lb_pad_x, pady=lb_pad_y,
           # width=lb_width, height=lb_height, anchor=lb_anchor,
           # relief=RAISED,  # включить обтекатель фона
           # bd=10  # толщина обтекателя
           # justify=LEFT  # выравнивать по краю
           )

count = 2


def testimine():
    x = randint(1, 10)
    print(x)


def new_label():
    x = randint(1, 10)
    label = Label(root, text=x)
    label.pack()


def counter():
    global count
    count += 1
    btn_nr_of_count['text'] = f"Number of count {count}"
    if count % 2 == 0:
        btn['state'] = DISABLED
        btn_ok_printout['state'] = DISABLED

    else:
        btn['state'] = NORMAL
        btn_ok_printout['state'] = NORMAL


def disable_all():
    btn['state'] = DISABLED
    btn_ok_printout['state'] = DISABLED
    btn_fff_printout['state'] = DISABLED
    btn_nr_of_count['state'] = DISABLED


def enable_all():
    btn['state'] = NORMAL
    btn_ok_printout['state'] = NORMAL
    btn_fff_printout['state'] = NORMAL
    btn_nr_of_count['state'] = NORMAL


btn = Button(root, text=btn_txt, command=testimine)
btn_ok_printout = Button(root, text=btn_txt, command=new_label)
btn_fff_printout = Button(root, text="fff", command=lambda: Label(root, text="fff").pack())
btn_nr_of_count = Button(root, text=f"Number of count {count}", command=counter, bg="red", activebackground="green")
btn_disable_all = Button(root, text="Disable all!", command=disable_all)
btn_enable_all = Button(root, text="Enable all!", command=enable_all)
btn1 = Button(root, text="text1")
btn2 = Button(root, text="text2")
btn3 = Button(root, text="text3")
btn4 = Button(root, text="text4")


# lb.pack()
# # btn.pack()
# btn_ok_printout.pack()
# btn_fff_printout.pack()
# btn_nr_of_count.pack()
# btn_disable_all.pack()
# btn_enable_all.pack()
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1)
# btn3.grid(row=1, column=0, columnspan=2, sticky="we")
# btn4.grid(row=0, column=2, rowspan=2, sticky="ns")


# for i in range(5):
#     for j in range(2):
#         Button(root, text=f"Button {i}.{j}").grid(row=i, column=j, sticky="we")

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty value")


def del_entry():
    name.delete(0, END)
    pwd.delete(0, END)


def submit():
    Label(root, text=name.get(), bg=bg_color).grid(row=3, column=0, sticky="w")
    Label(root, text=pwd.get(), bg=bg_color).grid(row=4, column=0, sticky="w")




Label(root, text="Name:").grid(row=0, column=0, sticky="w")
Label(root, text="Password:").grid(row=1, column=0, sticky="w")

pwd = Entry(root, show="*")
pwd.grid(row=1, column=1, sticky="w")

name = Entry(root)
name.grid(row=0, column=1, sticky="w")

Button(root, text="Get", command=get_entry).grid(row=2, column=0, sticky="w")
Button(root, text="Delete", command=del_entry).grid(row=2, column=1, sticky="w")
Button(root, text="Incert", command=lambda: name.insert(0, "Narva ")).grid(row=2, column=2, sticky="w")
Button(root, text="Submit", command=submit).grid(row=2, column=3, sticky="w")

# root.grid_columnconfigure(0, minsize=100)
# root.grid_columnconfigure(1, minsize=200)
root.mainloop()
