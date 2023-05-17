import random
from tkinter import *
from tkinter import ttk
import tkinter as tk

from Monstro import Monstro

batalha = Tk()


Squirtle = Monstro("agua", "Squirtle", 40, 65, 45, "C:/Users/ct67ca/Desktop/sdfjngdfg/sql-p.png", "Golpe de cauda", "Super borrifada")
Tepig = Monstro("fogo", "Tepig", 65, 45, 40, "C:/Users/ct67ca/Desktop/sdfjngdfg/tepig-p.png","Morder", "Lança chamas")
Treecko = Monstro("planta", "Treecko", 40, 45, 65, "C:/Users/ct67ca/Desktop/sdfjngdfg/treecko-p.png", "Arranhão", "Raio solar")
Ezodia = Monstro("fogo", "Ezodia", 1, 99999, 99999, "C:/Users/ct67ca/Desktop/sdfjngdfg/ezodia-p.png", "", "Obliterar")

class Tela_duelo(tk.Tk):
    def __init__(self, user_pokemon, pokemon_ini) -> None:
        self.batalha = batalha
        self.user_pokemon = user_pokemon
        self.pokemon_ini = pokemon_ini
        self.interface()
        self.frames()
        self.labels()
        self.buttons()
        self.img()
        batalha.mainloop()

    def interface(self):
        self.batalha.title("Game Boy")
        self.batalha.configure(background="#F0F0E8")
        self.batalha.geometry("600x900")
        self.batalha.resizable(True, True)
        self.batalha.maxsize(width=600, height=900)
        self.batalha.minsize(width=600, height=900)
        

    def frames(self):
        self.tela = Frame(self.batalha, bg="#3d3c48")
        self.tela.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.70)
        
        self.frame_0 = Frame(self.tela, bg="#F8F8F8")
        self.frame_0.place(relx=0.05, rely=0.04, relwidth=0.90, relheight=0.70)

        self.frame_1 = Frame(self.frame_0, bg="#bcc1c4")
        self.frame_1.place(relx=0.60, rely=0.72, relwidth=0.35, relheight=0.15)

        self.frame_2 = Frame(self.frame_0, bg="#bcc1c4")
        self.frame_2.place(relx=0.05, rely=0.05, relwidth=0.35, relheight=0.15)

        self.frame_3 = Frame(self.tela, bg="#848687")
        self.frame_3.place(relx=0.05, rely=0.70, relwidth=0.90, relheight=0.15)

        self.frame_4 = Frame(self.frame_3, bg="#bcc1c4")
        self.frame_4.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.92)


    def labels(self):
        self.nome_meu_lb = Label(self.frame_1, text=self.user_pokemon.nome, bg="#bcc1c4", fg="#000", font=50)
        self.nome_meu_lb.place(relx=0.10, rely=0.10, relwidth=0.35, relheight=0.30)

        self.vidam_meu_lb = Label(self.frame_1, text=f"{self.user_pokemon.vida_maxima}/", bg="#bcc1c4", fg="#000", font=50)
        self.vidam_meu_lb.place(relx=0.10, rely=0.50, relwidth=0.15, relheight=0.25)

        self.vidaa_meu_lb = Label(self.frame_1, text=self.user_pokemon.vida, bg="#bcc1c4", fg="#000", font=50)
        self.vidaa_meu_lb.place(relx=0.25, rely=0.50, relwidth=0.09, relheight=0.25)

        self.risco_meu_lb = Label(self.frame_1, text="", bg="#000", fg="#000", font=50)
        self.risco_meu_lb.place(relx=0.40, rely=0.90, relwidth=0.60, relheight=0.05)

        self.nome_ini_lb = Label(self.frame_2, text=self.pokemon_ini.nome, bg="#bcc1c4", fg="#000", font=50)
        self.nome_ini_lb.place(relx=0.10, rely=0.10, relwidth=0.35, relheight=0.30)

        self.vidam_ini_lb = Label(self.frame_2, text=f"{self.pokemon_ini.vida_maxima}/", bg="#bcc1c4", fg="#000", font=50)
        self.vidam_ini_lb.place(relx=0.10, rely=0.50, relwidth=0.15, relheight=0.25)

        self.vidaa_ini_lb = Label(self.frame_2, text=self.pokemon_ini.vida, bg="#bcc1c4", fg="#000", font=50)
        self.vidaa_ini_lb.place(relx=0.25, rely=0.50, relwidth=0.09, relheight=0.25)

        self.risco_ini_lb = Label(self.frame_2, text="", bg="#000", fg="#000", font=50)
        self.risco_ini_lb.place(relx=0.35, rely=0.90, relwidth=0.65, relheight=0.05)

        """self.status_lb = Label(self.frame_4, text="", bg="#bcc1c4", fg="#fff", font=90)
        self.status_lb.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.25)"""

    def img(self):
        self.user_image = tk.PhotoImage(file=self.user_pokemon.rosto)
        self.user_label = tk.Label(self.frame_0, image=self.user_image)
        self.user_label.place(x=80, y=200)

        self.ini_image = tk.PhotoImage(file=self.pokemon_ini.rosto)
        self.ini_label = tk.Label(self.frame_0, image=self.ini_image)
        self.ini_label.place(x=320, y=25)

        self.botao_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/botao.png")
        self.botao_label = tk.Label(self.batalha, image=self.botao_image)
        self.botao_label.place(x=15, y=650)

        self.pause_image = tk.PhotoImage(file="C:/Users/ct67ca/Desktop/sdfjngdfg/pause.png")
        self.pause_label = tk.Label(self.batalha, image=self.pause_image)
        self.pause_label.place(x=250, y=790)


    def buttons(self):
        if self.user_pokemon.tipo == "fogo":
            bg = "#FF9D55"
        if self.user_pokemon.tipo == "agua":
            bg = "#5090D6"
        if self.user_pokemon.tipo == "planta":
            bg = "#34c776"

        if not self.user_pokemon.nome == "Ezodia":
            self.atk_normal_bt = Button(self.batalha, text=self.user_pokemon.ataque1,  bg="#bcc1c4", fg="#000")
            self.atk_normal_bt.place(relx=0.76, rely=0.77, relwidth=0.20, relheight=0.05)

            self.atk_tipo_bt = Button(self.batalha, text=self.user_pokemon.ataque2,  bg=bg, fg="#000")
            self.atk_tipo_bt.place(relx=0.65, rely=0.83, relwidth=0.20, relheight=0.05)
        else:
            self.atk_tipo_bt = Button(self.batalha, text=self.user_pokemon.ataque2,  bg=bg, fg="#000")
            self.atk_tipo_bt.place(relx=0.65, rely=0.83, relwidth=0.20, relheight=0.05)

    def ataque(self):
        pass

