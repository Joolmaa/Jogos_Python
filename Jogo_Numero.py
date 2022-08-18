import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")


    numero_secreto= round(random.randrange(1,101)) #0.0 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de difícudade?")
    print("(1)fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Defina um nível:\t"))
    if(nivel == 1):
        total_de_tentativas = 30
    elif(nivel == 2):
        total_de_tentativas = 20
    else:
        total_de_tentativas = 5    
    
    for rodada in range  (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas,))
        chute_int = input("Digite um número entre 1 e 100:\t")
        print("Você digitou:", chute_int)
        chute = int(chute_int)

        if(chute < 1 or chute > 100):
            print("Você só pode digitar um número entre 1 e 100!!!!")
            continue
        
        acertou = chute == numero_secreto
        errou_mais = chute > numero_secreto
        errou_menos = chute < numero_secreto

        if(acertou):
            print("Você acertou!E fez {} pontos".format(pontos))
            break
        else:
            if(errou_mais):
                print("Você errou!Você passou do número secreto\n")
            elif(errou_menos):
                print("Você errou!Você está perto do número secreto\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
            rodada = rodada + 1

    print("Fim de jogo;-;")

if(__name__ == "__main__"):
    jogar()
                
                
    
