import tkinter
from tkinter import *
from tkinter import filedialog
import buildAutomata
import pushdownAutomata
from PIL import ImageTk, Image
import os

gui = Tk()
gui.title("Intepretador de autômatos")
gui.geometry("800x500")
hasSelected = IntVar()
hasSelected.set(0)
automataType = StringVar() #Variavel de escolha do tipo de automato
automataType.set(None) #Iniciamos ela com None para nao escolher nenhuma opcao na inicalizacao

#Classe que cuida da leitura das palavras que serão verificasa
class inputWord():
    def createWindow(self, filePath, automataType):
        if automataType.get() == "AFN":
            buildAutomata.afnBuild(filePath)
        elif automataType.get() == "AFD":
            buildAutomata.afdBuild(filePath)
        elif automataType.get() == "AP":
            pushdownAutomata.read_automato_from_txt(filePath)
        top = Toplevel()
        top.geometry()
        self.frame = Frame(top)
        self.frame.pack()

        #Cria todos os elementos que serao utilizados na janela
        wordTitle = Label(top, text="Insira as palavras que deseja testar", font=('Arial 14'))
        input = Entry(top)
        wordInserted = Label(top, text="")
        acceptMessage = Label(top, text="")
        send = Button(top, text="Continuar", command=lambda: onClick(input, acceptMessage, wordInserted))
        if automataType.get() == "AP":
            imgMessage = Label(top, text="Visualização de autômato não disponível para AP", font=('Arial 12'))
        else:
            imgFile = ImageTk.PhotoImage(Image.open("automata.png"))
            imgShow = Label(top, image=imgFile)
            imgShow.image = imgFile

        #Funcao que testa o automato e mostra na tela de foi aceito ou nao
        def onClick(word, acceptMessage, wordInserted):
            wordInserted.configure(text="Palavra que foi testada: "+word.get())

            accept = "" #Criando variavel

            if automataType.get() == "AFN":
                accept = buildAutomata.afnRun(word.get())
            elif automataType.get() == "AFD":
                accept = buildAutomata.afdRun(word.get())
            elif automataType.get() == "AP":
                accept = pushdownAutomata.apRun(word.get())
            if accept:
                acceptMessage.configure(text="Aceito", fg="#228B22", font="Arial 10 bold")
            else:
                acceptMessage.configure(text="Não aceito", fg="#C70039", font="Arial 10 bold")

        #Insere os elementos na janela
        wordTitle.pack()
        input.pack()
        send.pack()
        if automataType.get() == "AP":
            imgMessage.pack()
        else:
            imgShow.pack()
        acceptMessage.pack()
        wordInserted.pack()

count = 0 #Essa variavel verifica se uma opcao ja foi selecionada
def uploadButton():
    global count
    count +=1

    #So colocar o botao na tela apos selecionar pela primeira vez uma das opcoes (AFD ou AFN)
    if count == 1:
        if automataType.get() != None:
            upload = tkinter.Button(mainFrame, text="Selecionar arquivo", command=lambda: openFile())
            upload.pack()
def openFile():
    gui.filename = filedialog.askopenfilename(title="Abrir arquivo", filetypes=[("Arquivos de texto","*.txt")])
    word = inputWord()
    word.createWindow(gui.filename, automataType)

def closeApp():
    if os.path.isfile("automata.png"):
        os.remove("automata.png")
    gui.destroy()

mainFrame = Frame(gui)
title = Label(mainFrame, text="Olá! Bem vindo!", font=('Arial 18')).pack()
subtitle = Label(mainFrame, text="Insira um arquivo para começar", font=('Arial 14')).pack()
afnButton = Radiobutton(mainFrame, text="AFN", variable=automataType, value="AFN", command=uploadButton).pack()
afdButton = Radiobutton(mainFrame, text="AFD", variable=automataType, value="AFD", command=uploadButton).pack()
apButton = Radiobutton(mainFrame, text="AP", variable=automataType, value="AP", command=uploadButton).pack()

mainFrame.place(rely=0.4, relx=0.5, anchor=CENTER)
gui.protocol("WM_DELETE_WINDOW", closeApp)
mainloop()