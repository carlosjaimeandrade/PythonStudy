import tkinter

class App:

    def __init__(self, title,  y):
        window = tkinter.Tk()
        window.title(title)
        window.minsize(width=x,height=y)
        window.mainloop()

obj = App("x,window", 360, 640)
obj2 = App("window", 660, 640)