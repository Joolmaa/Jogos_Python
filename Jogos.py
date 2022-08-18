import Jogo_Forca
import Jogo_Numero

def escolha_jogos():
    print("********************************")
    print("*******Escolha o seu jogo!******")
    print("********************************")

    print("(1)foca  (2)adivinhcão")

    jogo = int(input("Qual é o jogo? "))

    if(jogo == 1):
        print("Jogo forca")
        Jogo_Forca.jogar()
    elif(jogo == 2):
        print("Jogo Adivinhação")
        Jogo_Numero.jogar()

if(__name__ == "__main__"):
    escolha_jogos()      