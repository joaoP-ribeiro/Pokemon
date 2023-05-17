import random
from tkinter import *
from tkinter import ttk
import tkinter as tk

from Monstro import Monstro
from campo_batalha import Tela_duelo

escolha = Tk()


Squirtle = Monstro("agua", "Squirtle", 40, 65, 45, "C:/Users/ct67ca/Desktop/sdfjngdfg/sql-p.png", "Golpe de cauda", "Super borrifada")
Tepig = Monstro("fogo", "Tepig", 65, 45, 40, "C:/Users/ct67ca/Desktop/sdfjngdfg/tepig-p.png","Morder", "Lança chamas")
Treecko = Monstro("planta", "Treecko", 40, 45, 65, "C:/Users/ct67ca/Desktop/sdfjngdfg/treecko-p.png", "Arranhão", "Raio solar")
Ezodia = Monstro("fogo", "Ezodia", 1, 99999, 99999, "C:/Users/ct67ca/Desktop/sdfjngdfg/sql-p.png", "", "Obliterar")


class Tela_escolha(tk.Tk):
    def __init__(self) -> None:
        self.escolha = escolha
        self.selecao = False
        self.interface()
        self.frames()
        self.labels()
        self.buttons()
        self.img()
        escolha.mainloop()
    

    def interface(self):
        self.escolha.title("Escolho você")
        self.escolha.configure(background="#7289D9")
        self.escolha.geometry("800x500")
        self.escolha.resizable(True, True)
        self.escolha.maxsize(width=800, height=500)
        self.escolha.minsize(width=800, height=500)

    def frames(self):
        self.frame_0 = Frame(self.escolha, bg="#fff")
        self.frame_0.place(relx=0.02, rely=0.25, relwidth=0.20, relheight=0.50)

        self.frame_1 = Frame(self.escolha, bg="#fff")
        self.frame_1.place(relx=0.28, rely=0.25, relwidth=0.20, relheight=0.50)

        self.frame_2 = Frame(self.escolha, bg="#fff")
        self.frame_2.place(relx=0.53, rely=0.25, relwidth=0.20, relheight=0.50)

        self.frame_3 = Frame(self.escolha, bg="#fff")
        self.frame_3.place(relx=0.78, rely=0.25, relwidth=0.20, relheight=0.50)

    def labels(self):
        self.escolha_lb = Label(self.escolha, text="ESCOLHA SEU POKEMON!", bg="#7289D9", fg="#000")
        self.escolha_lb.place(relx=0.05, rely=0.10, relwidth=0.94, relheight=0.05)

        
    def buttons(self):
        self.squitle_bt = Button(self.frame_0, text="ESCOLHO VOCÊ",  bg="#5090D6", fg="#000", command=self.squirtle)
        self.squitle_bt.place(relx=0.15, rely=0.80, relwidth=0.7, relheight=0.15)

        self.tepig_bt = Button(self.frame_1, text="ESCOLHO VOCÊ",  bg="#FF9D55", fg="#000", command=self.tepig)
        self.tepig_bt.place(relx=0.15, rely=0.80, relwidth=0.7, relheight=0.15)

        self.treecko_bt = Button(self.frame_2, text="ESCOLHO VOCÊ",  bg="#34c776", fg="#000", command=self.treecko)
        self.treecko_bt.place(relx=0.15, rely=0.80, relwidth=0.7, relheight=0.15)

        self.ezodia_bt = Button(self.frame_3, text="ESCOLHO VOCÊ",  bg="#DEDB63", fg="#000", command=self.ezodia)
        self.ezodia_bt.place(relx=0.15, rely=0.80, relwidth=0.7, relheight=0.15)
    
    def img(self):
        self.squirtle_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/sql.png")
        self.tepig_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/tepig.png")
        self.treecko_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/treecko.png")
        self.ezodia_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/ezodia.png")

        self.squirtle_label = tk.Label(self.frame_0, image=self.squirtle_image)
        self.squirtle_label.place(x=1, y=2)

        self.tepig_label = tk.Label(self.frame_1, image=self.tepig_image)
        self.tepig_label.place(x=1, y=2)

        self.treecko_label = tk.Label(self.frame_2, image=self.treecko_image)
        self.treecko_label.place(x=1, y=2)

        self.ezodia_label = tk.Label(self.frame_3, image=self.ezodia_image)
        self.ezodia_label.place(x=1, y=2)
    
    def escolha_inimigo(self, meu_pokemon=""):
        pokemons = [Squirtle, Tepig, Treecko]
        try:
            remover = pokemons.index(meu_pokemon)
            del pokemons[remover]
        except:
            ...
        pokemon_ini = random.choice(pokemons)
        pokemon_ini.bot = True
        return pokemon_ini

    
    def squirtle(self):
        if not self.selecao:
            pokemon_ini = self.escolha_inimigo(Squirtle)
            self.selecao = True
            Tela_duelo(Squirtle, pokemon_ini )
        else:
            print("pokemon ja escolhido")

    def tepig(self):
        if not self.selecao:
            pokemon_ini = self.escolha_inimigo(Tepig)
            self.selecao = True
            Tela_duelo(Tepig, pokemon_ini )
        else:
            print("pokemon ja escolhido")
    
    def treecko(self):
        if not self.selecao:
            pokemon_ini = self.escolha_inimigo(Treecko)
            self.selecao = True
            Tela_duelo(Treecko, pokemon_ini )
        else:
            print("pokemon ja escolhido")
    
    def ezodia(self):
        if not self.selecao:
            pokemon_ini = self.escolha_inimigo()
            self.selecao = True
            Tela_duelo(Ezodia, pokemon_ini )
        else:
            print("pokemon ja escolhido")


tl = Tela_escolha()