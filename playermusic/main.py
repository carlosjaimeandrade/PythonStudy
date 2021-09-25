from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os
import pygame


class Player:
    def __init__(self):

        self.local = ''
        self.status = 0
        pygame.mixer.init()

        self.window = ThemedTk(theme='equilux')
        self.window.title('Music Player')
        self.window.resizable(0, 0)
        self.window.geometry("300x500+500+200")
        self.window.config(bg='#444444')

        self.img_add = PhotoImage(file='add.png')
        self.img_next = PhotoImage(file='next.png')
        self.img_pause = PhotoImage(file='pause.png')
        self.img_previus = PhotoImage(file='previus.png')
        self.img_remove = PhotoImage(file='remove.png')
        self.img_play = PhotoImage(file='play.png')

        self.list = Listbox(self.window, bg='#555555', bd=0, height=16, fg='white', selectbackground='#a2ebcc')
        self.list.pack(fill='x', pady=10, padx=10) # dar paddding na lateral e em cima pady=10, padx=10

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)

        self.remove = ttk.Button(self.frame, image=self.img_remove, command=self.delete_music)
        self.remove.grid(row=0, column=0, padx=10)

        self.add = ttk.Button(self.frame, image=self.img_add, command=self.selectMusic)
        self.add.grid(row=0, column=1, padx=10)

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=10)

        self.review = ttk.Button(self.frame2, image=self.img_previus, command=self.previus_music)
        self.review.grid(row=0, column=0)

        self.play = ttk.Button(self.frame2, image=self.img_play, command=self.play_music)
        self.play.grid(row=0, column=1)

        self.next = ttk.Button(self.frame2,  image=self.img_next, command=self.next_music)
        self.next.grid(row=0, column=2)

        self.volume = ttk.Scale(self.window, from_=0, to=1, command=self.volume_set)
        self.volume.pack(fill="x", pady=10, padx=10)

        self.window.mainloop()

    def selectMusic(self):
        self.local = filedialog.askdirectory()
        file = os.listdir(self.local) #lista os arquivos que estõ dentro de uma pasta

        for arquivo in file:
            self.list.insert(END, str(arquivo)) #inserir dentro da pagina Listbox

    def delete_music(self):
        self.list.delete(ANCHOR) #ANCHOR indica icone selecionado

    def next_music(self):
        try:
            index = self.list.curselection()[0] + 1 #curseselection indica o numero que está selecionado
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_msg('Não tem proxima musica')
    def previus_music(self):
        try:
            index = self.list.curselection()[0] - 1
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_msg('Não tem musica antes')
    def play_music(self):
        try:
            if self.status == 0:
                pygame.mixer.music.load(str(self.local) + "/" + str(self.list.get(ANCHOR)))
                pygame.mixer.music.play()
                self.play.config(image=self.img_pause)
                self.status =1
            else:
                pygame.mixer.music.pause()
                self.play.config(image=self.img_play)
                self.status = 0
        except:
            self.error_msg('Musica não valida')
    def error_msg(self, menssage):
        window = Toplevel()
        window.title("error")
        window.geometry("300x100+100+200")
        window.resizable(0, 0)
        window.config(bg='#444444')

        text = ttk.Label(window, text=str(menssage))
        text.pack(expand=YES) #fica no meio expand

        btn= ttk.Button(window, text="  ok", command=window.destroy)
        btn.pack()

    def volume_set(self, var):
        pygame.mixer.music.set_volume(self.volume.get())
Player()