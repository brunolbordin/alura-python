import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade você deseja?")
    print("Nível (1) - Fácil\nNível (2) - Médio\nNível (3) - Díficil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    ##while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou o número secreto e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)  # 40 - 20 = 20
            pontos = pontos - pontos_perdidos
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Sua pontuação foi {}".format(numero_secreto, pontos))
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if rodada == total_de_tentativas:
                    print("O número secreto era {}. Sua pontuação foi {}".format(numero_secreto, pontos))

    print("Fim do Jogo!!!")


if __name__ == "__main__":
    jogar()
