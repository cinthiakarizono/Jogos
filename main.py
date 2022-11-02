import adivinhacao
import forca
def escolher_jogo():
    print("######################################")
    print("##########Escolha o seu jogo##########")
    print("######################################")

    print("(1) Jogo da adivinhação \n(2) Jogo da forca")
    opcao = int(input("Digite uma opção:"))

    if (opcao == 1):
        print("Jogo da adivinhação")
        adivinhacao.jogar()
    elif (opcao == 2):
        print("Jogo da forca")
        forca.jogar()
    else:
        print("Opção inválida")
if (__name__ == "__main__"):
    escolher_jogo()