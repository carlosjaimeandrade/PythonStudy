from tkinter import *
import pyscreenshot

class Paint:

    def __init__(self):
        self.window = Tk()
        self.window.title("paint")
        self.window.minsize(width=1280, height=720)
        self.window.resizable(0,0)

        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

        self.img_line = PhotoImage(file='icons/line.png') #trazer uma imagem
        self.img_oval = PhotoImage(file='icons/oval.png')  # trazer uma imagem
        self.img_eraser = PhotoImage(file='icons/eraser.png')  # trazer uma imagem
        self.img_save = PhotoImage(file='icons/save.png')  # trazer uma imagem
        self.img_square = PhotoImage(file='icons/square.png')  # trazer uma imagem
        self.img_new = PhotoImage(file='icons/new.png')  # trazer uma imagem

        self.color = ("black", 'gray', 'white', 'red', 'green', 'blue', 'purple')

        self.pick_color = "black"

        self.bar = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar.pack(fill='x') #fill preenche toda o width3

        self.text_color = Label(self.bar, text='  Colors:  ', fg='white', bg='#3b3b3b')
        self.text_color.pack(side='left')

        for i in self.color:
            self.button = Button(self.bar, bg=i, width=3, height=1, command=lambda col=i :self.select_color(col))
            self.button.pack(side='left')

        self.label_color = Label(self.bar, text=' color choose: ', fg='white', bg='#3b3b3b')
        self.label_color.pack(side='left')

        self.buton_color = Button (self.bar, image=self.img_square, bd=0, bg='red', command=self.selected)
        self.buton_color.pack(side='left')

        self.text_size = Label(self.bar, text=' Tamanho: ', fg='white', bg='#3b3b3b')
        self.text_size.pack(side='left')

        self.pen_size = Spinbox(self.bar, from_=1, to=50, width=5, )
        self.pen_size.pack(side='left')

        self.text_brushs = Label(self.bar, text='  brushs:  ', fg='white', bg='#3b3b3b')
        self.text_brushs.pack(side='left')

        self.button_line = Button(self.bar, image=self.img_line, bd=0, bg='red', command=self.bruch_line) #inserir imagem no botão.
        self.button_line.pack(side='left')
        self.button_oval = Button(self.bar, image=self.img_oval, bd=0, bg='red', command=self.bruch_oval) #inserir imagem no botão.
        self.button_oval.pack(side='left')
        self.button_eraser = Button(self.bar, image=self.img_eraser, bd=0, bg='red', command=self.bruch_eraser) #inserir imagem no botão.
        self.button_eraser.pack(side='left')

        self.text_options = Label(self.bar, text=' Tamanho: ', fg='white', bg='#3b3b3b')
        self.text_options.pack(side='left')
        self.button_save = Button(self.bar, image=self.img_save, bd=0, bg='red', command=self.save) #inserir imagem no botão.
        self.button_save.pack(side='left')
        self.button_new = Button(self.bar, image=self.img_new, bd=0, bg='red', command=self.clean) #inserir imagem no botão.
        self.button_new.pack(side='left')

        self.are_drew = Canvas(self.window,height=720, bg='gainsboro')
        self.are_drew.pack(fill='both') # fill='both' ele faz preencher  width e height completo
        self.are_drew.bind("<B1-Motion>", self.draw) #bind determina o evento como o pack mas para evento usa o bind

        self.window.bind("<F1>", self.clean) #adiciona o atalho
        self.window.bind("<F2>", self.save)
        self.window.mainloop()

    def draw(self, event): #evente determina que será entrada teclado e mause
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)

        if self.oval_brush:
            self.are_drew.create_oval(x1, y1, x2, y2, fill=self.pick_color, width=self.pen_size.get(),
                                      outline=self.pick_color)  # outline contorno
        elif self.line_brush:
            self.are_drew.create_oval(x1 - 10, y1 - 10, x2, y2, fill=self.pick_color, width=self.pen_size.get())  # outline contorno
        else:
            self.are_drew.create_oval(x1, y1, x2, y2, fill='gainsboro', width=self.pen_size.get(),
                                      outline='gainsboro')  # outline contorno

    def select_color(self, col):
        self.pick_color = col

    def bruch_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False
    def bruch_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False
    def bruch_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = False
    def clean(self, event):
        self.are_drew.delete('all')

    def save(self, event):

        x = self.window.winfo_rootx() + self.are_drew.winfo_x()
        y = self.window.winfo_rooty() + self.are_drew.winfo_y()
        x1 = self.window.winfo_rootx() + self.are_drew.winfo_width()
        y1 = self.window.winfo_rooty() + self.are_drew.winfo_height()

        img = pyscreenshot.grab(bbox=(x,y,x1,y1))
        img.save('img.jpeg', 'jpeg')


    def selected(self):
        print('teste')
Paint()


