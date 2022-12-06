from tkinter import Tk
from tkinter import PhotoImage

title = "Клавиатурный трженажер"

root = Tk()

photo = PhotoImage(file='ico-50.png')
root.iconphoto(False, photo)

root.config(bg="#dab894")
root.title(title)
root.geometry("500x200+400+500")
root.resizable(width=False, height=False)

root.mainloop()