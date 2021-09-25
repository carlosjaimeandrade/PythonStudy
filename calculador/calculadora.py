from tkinter import *

class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title("Calc")
        self.window.iconbitmap("img/logoF.ico")
        self.window.resizable(0,0) # não define o tamaho o width que definira

        self.scren_numbers = Entry(self.window, font="arial 20 bold", bg="#3f4c63", fg="white", width=14) # como se fosse o imput para digitarmos um valor fg alera a cor
        self.scren_numbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button1 = Button(self.frame, bg="orange", bd="0", text="1", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("1")) #bd tira a borda
        self.button2 = Button(self.frame, bg="orange", bd="0", text="2", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("2")) #bd tira a borda
        self.button3 = Button(self.frame, bg="orange", bd="0", text="3", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("3")) #bd tira a borda
        self.button4 = Button(self.frame, bg="orange", bd="0", text="4", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("4")) #bd tira a borda
        self.button5 = Button(self.frame, bg="orange", bd="0", text="5", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("5")) #bd tira a borda
        self.button6 = Button(self.frame, bg="orange", bd="0", text="6", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("6")) #bd tira a borda
        self.button7 = Button(self.frame, bg="orange", bd="0", text="7", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("7")) #bd tira a borda
        self.button8 = Button(self.frame, bg="orange", bd="0", text="8", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("8")) #bd tira a borda
        self.button9 = Button(self.frame, bg="orange", bd="0", text="9", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("9")) #bd tira a borda
        self.buttonadd = Button(self.frame, bg="orange", bd="0", text="+", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("+")) #bd tira a borda
        self.button_unincrease = Button(self.frame, bg="orange", bd="0", text="-", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("-")) #bd tira a borda
        self.button_division = Button(self.frame, bg="orange", bd="0", text="/", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("/")) #bd tira a borda
        self.button_multi = Button(self.frame, bg="orange", bd="0", text="*", font="arial", fg="white",
                              width=5, height=3, command=lambda: self.touch("*")) #bd tira a borda
        self.button_igual = Button(self.frame, bg="orange", bd="0", text="=", font="arial", fg="white", #lambda ele determina que só irá funcionar a função se for precionado o buton. isso se a função ter que entrar vvalor
                              width=11, height=3, command=self.total) #bd tira a borda
        self.button_clear = Button(self.frame, bg="orange", bd="0", text="C", font="arial", fg="white",
                              width=5, height=3, command=self.Clen) #bd tira a borda

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button_unincrease.grid(row=0, column=3)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button_division.grid(row=1, column=3)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.button_multi.grid(row=2, column=3)
        self.buttonadd.grid(row=3, column=3)
        self.button_clear.grid(row=3, column=2)
        self.button_igual.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def touch(self, num):
        self.scren_numbers.insert(END, num)
    def Clen(self):
        self.scren_numbers.delete(0,END)
    def total(self):
        t = eval(self.scren_numbers.get())
        self.scren_numbers.delete(0, END)
        self.scren_numbers.insert(0, str(t))

Calc()