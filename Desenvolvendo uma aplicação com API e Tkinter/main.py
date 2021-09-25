from tkinter import *
import requests
import json


class MovieData:

    def __init__(self):

        self.window = Tk()
        self.window.title('Movie Data')
        self.window.geometry("600x400+200+150")
        self.window.resizable(0, 0)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.text_entry = Entry(self.frame, font="arial 20", width=30)
        self.text_entry.grid(row=0, column=0)

        self.button_seash = Button(self.frame, text='serch', font="arial 16", command=self.procurar)
        self.button_seash.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack(fill=BOTH, expand=YES)
        self.window.mainloop()

    def procurar(self):
        try:
            request = requests.get("http://www.omdbapi.com/?t=" + self.text_entry.get() + "&apikey=3bf3e639")
            dict = json.loads(request.text)

            self.list.delete(0, END)
            self.list.insert(END, ("o titulo é" + dict['Title']))

        except:
            self.list.delete(0, END)
            self.list.insert(END, ("Movie não escontrado"))

MovieData()
