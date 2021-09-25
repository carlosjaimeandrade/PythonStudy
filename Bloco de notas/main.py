import tkinter


def NewFile():
    text_area.delete(1.0,"end")

def Save():
    container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()
def Open():
    file = open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)
def UpdateFont():
    size = spin_size.get() #size é a variavel que armazena o valor do Spinbox (caixa de opção) a informação GET significa PEGAR
    font = spin_font.get() #font é a variavel que armazena o valor do Spinbox (caixa de opção) a informação GET significa PEGAR
    text_area.config(font="{} {}".format(font, size)) #config atualiza as informação da varivevl TEXT_AREA adicionando uma nova font que está na varivel SIZE
    # os {} defini que existe um texto ali mas que pegará na variavel que esta de fora no .format




window = tkinter.Tk() #cria uma janela
window.title("FastMedia") #alterando o nome da janela
window.minsize(width=1280, height=720)#definir tamanho da janela
#ou
#window.geometry("1288x720")
#cria loop ja pronto do modulo.
#acessa a area para criar um texto

frame = tkinter.Frame(window, height=30)#cria uma janela de frame pense como uma "DIV"
frame.pack(fill='x')  # o fill faz o fram ficar responsivo

font_text = tkinter.Label(frame, text=' font: ') # A variavel frame significa onde será aplicado o label
font_text.pack(side="left") #side significa lado

spin_font = tkinter.Spinbox(frame, values=("Ariel", "Verdana")) #spinbox cria um box com escolhar
spin_font.pack(side="left")

font_size = tkinter.Label(frame, text=" Font size: ") # label abre um caixa de escrita
font_size.pack(side="left")

spin_size = tkinter.Spinbox(frame, from_=0, to=60) # o from endica "de"(FROM) 0 "ATE" (TO) o numero escolhido
spin_size.pack(side="left")

button_update = tkinter.Button(frame, text=" UP ", command=UpdateFont) # cria um botão.
button_update.pack(side="left")

text_area = tkinter.Text(window, font="Arial 20 bold",width=1280, height=720)
text_area.pack() #pega e Criar e adicioanr no window

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="new", command=NewFile)
file_menu.add_command(label="Salve", command=Save)
file_menu.add_command(label="open", command=Open)
file_menu.add_command(label="Exit", command=window.quit)
main_menu.add_cascade(label="File", menu=file_menu)


window.config(menu=main_menu) #adiciona o menu
window.mainloop()


