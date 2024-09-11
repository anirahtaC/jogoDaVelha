from itertools import combinations
from random import random
import time

print()
print("───────────────────────────────────")
print()
print("Bem-vindo ao Jogo da Velha!")
print()

#Menu do jogo
print("───────────────────────────────────")
print()
iniciar = input("Digite [S] para começar ou [N] para encerra nosso jogo: ")
print()
   
if iniciar == "S" or iniciar == "s": 
    print("O jogo começou! Espere um instante...")
    time.sleep(3)
    
else:
    print("───────────────────────────────────")
    print()
    print("O jogo foi encerrando... Aguarde...")
    print()
    time.sleep(3)
    print("Agradecemos a sua presença em nosso jogo! Até a próxima!")
    print("Feito por: Catharina Bonella, Luyz Castelo, Lucas Costa e Matheus Cerqueira.")
    print()
    print("───────────────────────────────────")
    quit()

print()

#Jogador X ou O
def jogadores():
    jogadores = int(random() * 10 % 2)

    if jogadores == 0:
        jogadores = "X"
    else:
        jogadores = "O"
    return jogadores

jogada = jogadores()


#Tabuleiro (1)
tabuleiro = [' ' for _ in range(9)]

def desenhar_tabuleiro():
    print()
    print(tabuleiro[0] + " ╿ " + tabuleiro[1] + " ╿ " + tabuleiro[2])
    print("╾───────╼")
    print(tabuleiro[3] + " │ " + tabuleiro[4] + " │ " + tabuleiro[5])
    print("╾───────╼")
    print(tabuleiro[6] + " ╽ " + tabuleiro[7] + " ╽ " + tabuleiro[8])
    print()
    print("───────────────────────────────────")
    print()
    print("É a vez de: Jogador ⊢ " + jogada + " ⊣")
    print()
acertos = ((0,1,2)), ((3,4,5)), ((6,7,8)), ((0,3,6)), ((1,4,7)), ((2,5,8)), ((0,4,8)), ((2,4,6))

#Verificar Ganhador
def verificar_ganhador():
    for acerto in acertos:
         if tabuleiro[acerto[0]] == tabuleiro[acerto[1]] == tabuleiro[acerto[2]] != " ":
            return True
    return False
 
#Verificar Empate
def verificar_empate():
    return " " not in tabuleiro


#Escolha de Casas
def escolher_casas():
    global jogada
    while True:
        escolha = int(input("Digite um número de (1 a 9) para escolher uma casa: "))
        print("")
        resposta = escolha
        if tabuleiro[resposta - 1] == " ":
            tabuleiro[resposta - 1] = jogada
            break
        else:
            print("Esta casa já foi preenchida, digite novamente!")
            print("")


#Começar jogo
if iniciar:
    while True:
        desenhar_tabuleiro()

        while True:
            escolher_casas()
            
            if jogada == "X":
                jogada = "O"
            else:
                jogada = "X"
                
            desenhar_tabuleiro()

            if verificar_ganhador():
                print()
                print(f"Parabéns, jogador {jogada}! Você ganhou a partida!")
                print()
                break
            if verificar_empate():
                print("Deu velha!! Ocorreu um empate!")
                print()
                break

        reiniciar = input("Gostaria de jogar novamente? Digite [S] para prosseguir ou [N] para encerrar: ")
        if reiniciar == "S" or reiniciar == "s":
            tabuleiro = [' ' for _ in range(9)]
        else:
            print()
            print("───────────────────────────────────")
            print()
            print("O jogo foi encerrado! Aguarde...")
            time.sleep(3)
            print()
            print("Agradecemos a sua presença em nosso jogo! Até a próxima!")
            print("Feito por: Catharina Bonella, Luyz Castelo, Lucas Costa e Matheus Cerqueira.")
            print()
            print("───────────────────────────────────")
            break
