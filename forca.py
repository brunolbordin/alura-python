import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao Jogo de Força!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    posicao_da_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao_da_palavra].upper()
    return palavra_secreta


def inicializa_letras_acertardas(palavra):
    return ["_" for letra in palavra]


def recebe_resposta_do_usuario():
    resposta_do_usuario = input("Digite uma letra:")
    resposta_do_usuario = resposta_do_usuario.strip().upper()
    return resposta_do_usuario


def adiciona_resposta_correta_no_letras_acertadas(resposta_do_usuario, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if resposta_do_usuario == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Parabéns. Você acertou a palavra secreta!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu, a palavra secreta era {}".format(palavra_secreta))
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("Você errou a letra")
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertardas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:
        resposta_do_usuario = recebe_resposta_do_usuario()

        if resposta_do_usuario in palavra_secreta:
            adiciona_resposta_correta_no_letras_acertadas(resposta_do_usuario, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)
            if tentativas == 6:
                print("Última tentativa !!!")

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


if __name__ == "__main__":
    jogar()
