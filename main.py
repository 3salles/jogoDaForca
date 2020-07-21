from tkinter import *
import tkinter as telaJogo
from tkinter import messagebox
from string import ascii_uppercase
import random

# Importando janela do Tkinter
window = telaJogo.Tk()
window.title("Jogo da Forca - Animais")

palavras = ['CACHORRO', 'GATO', 'COBRA', 'CAVALO', 'RAPOSA', 'URSO', 'COELHO', 'SAPO', 'LEOPARDO']

# Imagens da forca
imagens = [
  PhotoImage(file = "imagens/hang0.png"), PhotoImage(file = "imagens/hang1.png"), PhotoImage(file = "imagens/hang2.png"), PhotoImage(file = "imagens/hang3.png"),
  PhotoImage(file = "imagens/hang4.png"), PhotoImage(file = "imagens/hang5.png"), PhotoImage(file = "imagens/hang6.png"), PhotoImage(file = "imagens/hang7.png"),
  PhotoImage(file = "imagens/hang8.png"), PhotoImage(file = "imagens/hang9.png"), PhotoImage(file = "imagens/hang10.png"), PhotoImage(file = "imagens/hang11.png")
]

imgLabel = Label(window)
imgLabel.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 40)
imgLabel.config(image = imagens[0])

# Teclado do jogo
lblWord = StringVar()
Label(window, textvariable = lblWord, font = ("Consolas 24 bold")).grid(row = 0, column = 3, columnspan = 6, padx = 10)

i = 0
for c in ascii_uppercase:
  Button(window, text = c, command = lambda c = c: adivinhar(c), font = ("Helvetica 18"), width = 4).grid(row = 1+i//9, column = i%9)
  i += 1

# Novo Jogo
Button(window, text = "Novo\nJogo", command = lambda: novoJogo(), font =  ("Helvetica 10 bold")).grid(row = 3, column = 8, sticky = "NSWE")

# Função do Jogo
def novoJogo():
  global palavraComEspaco
  global tentativas
  tentativas = 0
  imgLabel.config(image = imagens[0])
  palavra = random.choice(palavras)
  palavraComEspaco =  " ".join(palavra)
  lblWord.set(" ".join("_"*len(palavra)))

# Função adivinhar
def adivinhar(letra):
  global tentativas
  if (tentativas < 11):
    texto = list(palavraComEspaco)
    adivinhou = list(lblWord.get())
    if (palavraComEspaco.count(letra) > 0):
      for c in range(len(texto)):
        if (texto[c] == letra):
          adivinhou[c] = letra
        lblWord.set("".join(adivinhou))
        if (lblWord.get() == palavraComEspaco):
          messagebox.showinfo("Jogo da Forca","Você Ganhou!")
          novoJogo()
    else:
      tentativas += 1
      imgLabel.config(image = imagens[tentativas])
      if (tentativas == 11):
        messagebox.showwarning("Jogo da Forca","Você Perdeu!")

# Chamando a janela
novoJogo()
window.mainloop()
