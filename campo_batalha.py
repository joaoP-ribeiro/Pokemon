import random
from tkinter import *
from tkinter import ttk
import tkinter as tk

from Monstro import Monstro

batalha = Tk()


Squirtle = Monstro("agua", "Squirtle", 40, 65, 45, "Golpe de cauda", "Super borrifada")
Tepig = Monstro("fogo", "Tepig", 65, 45, 40, "Morder", "Lança chamas")
Treecko = Monstro("planta", "Treecko", 40, 45, 65, "Arranhão", "Raio solar")


class Tela_duelo(tk.Tk):
    def __init__(self, user_pokemon, pokemon_ini) -> None:
        self.batalha = batalha
        self.user_pokemon = user_pokemon
        self.pokemon_ini = pokemon_ini
        self.interface()
        self.frames()
        self.labels()
        self.buttons()
        batalha.mainloop()

    def interface(self):
        self.batalha.title("Game Boy")
        self.batalha.configure(background="#F0F0E8")
        self.batalha.geometry("600x900")
        self.batalha.resizable(True, True)

    def frames(self):
        self.frame_0 = Frame(self.batalha, bg="#2F3D4F")
        self.frame_0.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.55)

        self.frame_1 = Frame(self.frame_0, bg="#fff")
        self.frame_1.place(relx=0.60, rely=0.65, relwidth=0.35, relheight=0.10)

        self.frame_2 = Frame(self.frame_0, bg="#fff")
        self.frame_2.place(relx=0.05, rely=0.05, relwidth=0.35, relheight=0.10)

        self.frame_3 = Frame(self.batalha, bg="#D4AA46")
        self.frame_3.place(relx=0.05, rely=0.58, relwidth=0.89, relheight=0.15)

        self.frame_4 = Frame(self.frame_3, bg="#23506D")
        self.frame_4.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.92)

        self.frame_5 = Frame(self.batalha, bg="#075FE7")
        self.frame_5.place(relx=0.05, rely=0.75, relwidth=0.89, relheight=0.22)

        self.frame_6 = Frame(self.frame_5, bg="#F8F8F8")
        self.frame_6.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.92)

    def labels(self):
        self.nome_meu_lb = Label(self.frame_1, text=self.user_pokemon.nome, bg="#fff", fg="#000", font=50)
        self.nome_meu_lb.place(relx=0.10, rely=0.10, relwidth=0.30, relheight=0.25)

        self.vidam_meu_lb = Label(self.frame_1, text=f"VIDA:{self.user_pokemon.vida_maxima}/", bg="#fff", fg="#000", font=50)
        self.vidam_meu_lb.place(relx=0.10, rely=0.45, relwidth=0.35, relheight=0.25)

        self.vidaa_meu_lb = Label(self.frame_1, text=self.user_pokemon.vida, bg="#fff", fg="#000", font=50)
        self.vidaa_meu_lb.place(relx=0.45, rely=0.45, relwidth=0.09, relheight=0.25)

        self.nome_ini_lb = Label(self.frame_2, text=self.pokemon_ini.nome, bg="#fff", fg="#000", font=50)
        self.nome_ini_lb.place(relx=0.10, rely=0.10, relwidth=0.30, relheight=0.25)

        self.vidam_ini_lb = Label(self.frame_2, text=f"VIDA:{self.pokemon_ini.vida_maxima}/", bg="#fff", fg="#000", font=50)
        self.vidam_ini_lb.place(relx=0.10, rely=0.45, relwidth=0.35, relheight=0.25)

        self.vidaa_ini_lb = Label(self.frame_2, text=self.pokemon_ini.vida, bg="#fff", fg="#000", font=50)
        self.vidaa_ini_lb.place(relx=0.45, rely=0.45, relwidth=0.09, relheight=0.25)

        self.status_lb = Label(self.frame_4, text="", bg="#23506D", fg="#fff", font=90)
        self.status_lb.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.25)

    def buttons(self):
        if self.user_pokemon.tipo == "fogo":
            bg = "#FF9D55"
        if self.user_pokemon.tipo == "agua":
            bg = "#5090D6"
        if self.user_pokemon.tipo == "planta":
            bg = "#34c776"

        self.atk_normal_bt = Button(self.frame_6, text=self.user_pokemon.ataque1,  bg="#bcc1c4", fg="#000")
        self.atk_normal_bt.place(relx=0.05, rely=0.40, relwidth=0.30, relheight=0.30)

        self.atk_tipo_bt = Button(self.frame_6, text=self.user_pokemon.ataque2,  bg=bg, fg="#000")
        self.atk_tipo_bt.place(relx=0.62, rely=0.40, relwidth=0.30, relheight=0.30)




tl = Tela_duelo(Treecko, Squirtle)