from tkinter import Tk, Checkbutton, Button, IntVar, StringVar

root = Tk()

over_18 = StringVar()
commercial = IntVar()

over_18.set('No')


root.geometry("300x300+150+150")
root.title("My first app")
bt = Checkbutton(root, text="Are you Deniss?", variable=over_18, offvalue='No', onvalue='Yes')

ads = Checkbutton(root, text="Do you want to see ADs??", variable=commercial, offvalue=0, onvalue=1)
sub = Checkbutton(root, text="Did you subscribe to me?", indicatoron=False)
bt.pack()
ads.pack()
sub.pack()


def select_all():
    for button in (bt, ads, sub):
        button.select()


def deselect_all():
    for button in (bt, ads, sub):
        button.deselect()


def toggle_all():
    for button in (bt, ads, sub):
        button.toggle()


def show():
    print('18', over_18.get())
    print('ads', commercial.get())

Button(root, text="Enter", command=select_all).pack()
Button(root, text="Deselect", command=deselect_all).pack()
Button(root, text="Deselect", command=toggle_all).pack()
Button(root, text="Show", command=show).pack()

root.mainloop()
