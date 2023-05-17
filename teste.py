import tkinter as tk

class PokemonBattle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Batalha Pokémon")
        self.geometry("800x600")
        
        self.background_image = tk.PhotoImage(file="C:/Users/João Pedro/OneDrive/Área de Trabalho/tela/imagens/campo.png")
        self.pokemon1_image = tk.PhotoImage(file="C:/Users/João Pedro/OneDrive/Área de Trabalho/tela/imagens/sql.png")
        self.pokemon2_image = tk.PhotoImage(file="C:/Users/João Pedro/OneDrive/Área de Trabalho/tela/imagens/tepig.png")
        
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.pokemon1_label = tk.Label(self, image=self.pokemon1_image)
        self.pokemon1_label.place(x=100, y=200)
        
        self.pokemon2_label = tk.Label(self, image=self.pokemon2_image)
        self.pokemon2_label.place(x=500, y=200)
        
        self.attack_button = tk.Button(self, text="Ataque", command=self.attack)
        self.attack_button.place(x=350, y=500)
        
    def attack(self):
        # Lógica do ataque do Pokémon
        
        # Exemplo de atualização da interface após o ataque
        self.pokemon1_image = tk.PhotoImage(file="C:/Users/João Pedro/OneDrive/Área de Trabalho/tela/imagens/sql.png")
        self.pokemon1_label.configure(image=self.pokemon1_image)
        
        self.pokemon2_image = tk.PhotoImage(file="C:/Users/João Pedro/OneDrive/Área de Trabalho/tela/imagens/tepig.png")
        self.pokemon2_label.configure(image=self.pokemon2_image)

if __name__ == "__main__":
    app = PokemonBattle()
    app.mainloop()
