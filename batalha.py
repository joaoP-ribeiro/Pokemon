import random
from time import sleep

import inquirer

from Monstro import Monstro


Magikarp = Monstro("agua", "Magikarp", 20, 10, 80,"Golpe de cauda", "Super borrifada")
Tepig = Monstro("fogo", "Tepig", 65, 63, 45,"Morder", "Lança chamas")
Treecko = Monstro("planta", "Treecko", 40, 45, 70, "Arranhão", "Raio solar")


def traco():
     print("____________________")

def qual_pokemon(pokemon):
    """
    Retorna o pokemon escolhido
    :param pokemon: str
    :return: var
    """
    match pokemon["poke"]:
        case "Magikarp":
                var = Magikarp
        case "Tepig":
                var = Tepig
        case "Treecko":
                var = Treecko
    return var


     

def escolha_ataques(var, var2):
    if var.bot:
        ataque=[1,2]
        escolha = random.choice(ataque)
        match escolha:
            case 1:
                dano, tipo = var.ataque_normal(var2.vida_maxima)

            case 2:
                dano, tipo = var.ataque_tipo(var2.vida_maxima, var2.vida)

    else:
        print("Escolha seu ataque!")
        questions = [
            inquirer.List("atq",
                          message="Ataques",
                          choices=[var.ataque1, var.ataque2],
                          ),
        ]
        ataque = inquirer.prompt(questions)
        match ataque["atq"]:
            case var.ataque1:
                dano, tipo = var.ataque_normal(var2.vida_maxima)

            case var.ataque2:
                dano, tipo = var.ataque_tipo(var2.vida_maxima, var2.vida)

    return dano, tipo

def duelo(meu_pokemon, pokemon_inimigo):
     """

     :param primeiro:
     :param segundo:
     :return:
     """
     if meu_pokemon.velocidade > pokemon_inimigo.velocidade:
        print(f"{meu_pokemon.treinador} você vai começar...")
        sleep(1)
        print(f"{meu_pokemon.treinador}... {meu_pokemon.nome} eu escolho você!...")
        sleep(1)
        print(f"{pokemon_inimigo.treinador}... {pokemon_inimigo.nome} eu escolho você!")
        sleep(1)
        while True:
            dano, tipo = escolha_ataques(meu_pokemon, pokemon_inimigo)
            pokemon_inimigo.perca_vida(dano, tipo)

            sleep(1)
            traco()
            meu_pokemon.status_atual()
            traco()
            pokemon_inimigo.status_atual()
            traco()
            sleep(1)

            if pokemon_inimigo.vida <=0:
                traco()
                meu_pokemon.status_atual()
                traco()
                pokemon_inimigo.status_atual()
                traco()
                print(f"parabéns {meu_pokemon.treinador} você venceu")
                break
            else:
                    pass
            
            sleep(1)
            print("Vez do oponente...")
            dano, tipo = escolha_ataques(pokemon_inimigo, meu_pokemon)
            meu_pokemon.perca_vida(dano, tipo)

            sleep(1)
            if meu_pokemon.vida <=0:
                traco()
                meu_pokemon.status_atual()
                traco()
                pokemon_inimigo.status_atual()
                traco()
                print(f"parabéns {pokemon_inimigo.treinador} você venceu")
                break
            else:
                    pass

     else:
        print(f"{pokemon_inimigo.treinador} você vai começar...")
        sleep(1)
        print(f"{meu_pokemon.treinador}... {meu_pokemon.nome} eu escolho você!...")
        sleep(1)
        print(f"{pokemon_inimigo.treinador}... {pokemon_inimigo.nome} eu escolho você!")
        print("\n")
        while True:
            dano, tipo = escolha_ataques(pokemon_inimigo, meu_pokemon)
            meu_pokemon.perca_vida(dano, tipo)

            sleep(1)
            traco()
            meu_pokemon.status_atual()
            traco()
            pokemon_inimigo.status_atual()
            traco()
            sleep(1)

            if meu_pokemon.vida <=0:
                traco()
                meu_pokemon.status_atual()
                traco()
                pokemon_inimigo.status_atual()
                traco()
                print(f"parabéns {meu_pokemon.treinador} você venceu")
                break
            
            sleep(1)
            print("Vez do oponente...")
            dano, tipo = escolha_ataques(meu_pokemon, pokemon_inimigo)
            pokemon_inimigo.perca_vida(dano, tipo)

            sleep(1)
            if pokemon_inimigo.vida <=0:
                traco()
                meu_pokemon.status_atual()
                traco()
                pokemon_inimigo.status_atual()
                traco()
                print(f"parabéns {pokemon_inimigo.treinador} você venceu")
                break
            
             
        
        
        




