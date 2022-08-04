import forca
import adivinhacao


def escolha_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("Opção (1) - Jogo da Forca\nOpção (2) - Jogo da Adivinhação")
    jogo = int(input("Qual jogo vocẽ quer jogar? "))

    if jogo == 1:
        print("Jogando jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando jogo da Adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolha_jogo()
