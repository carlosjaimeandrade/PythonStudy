import tkinter

class App:
    def __init__(self):
        self.valor = 20

        self.window = tkinter.Tk()
        self.window.title("marcador")
        self.window.minsize(width="360", height=640)
        self.window.maxsize(width="360", height=640)

        self.text = tkinter.Label(self.window,text="20", font="Arial 50 bold", pady=20) #pady pading
        self.text.pack()

        self.frame = tkinter.Frame(self.window, bg='white') # o fram cria um container para div
        self.frame.pack()

        self.button = tkinter.Button(self.frame, text="UP", bg="orange", width="20", command=self.Plus) #bg define a cor
        self.button.pack(side='left') #side define onde o botão ira ficar

        self.button2 = tkinter.Button(self.frame, text="DOWN", bg="orange", width="20", command=self.Down)
        self.button2.pack()



        self.window.mainloop()

    def Plus(self):
        if self.valor <20:
            self.valor +=1
            self.text.config(text="{}".format(self.valor))
    def Down(self):
        if self.valor > 0:
            self.valor -=1
            self.text.config(text="{}".format(self.valor))

App()