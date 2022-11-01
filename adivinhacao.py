import random

print("#############################################")
print("Olá! Seja bem vindo ao jogo de adivinhação!")
print("#############################################")

numero_secreto = int(random.randrange(1, 101))
rodada = 1
total_de_tentativas = 3
pontos = 1000
print("Qual o nível de dificuldade?")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Defina o nível:"))
if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

while (rodada <= total_de_tentativas):

    print("Tentativa ", rodada, "de ", total_de_tentativas)
    chute_str = input("Digite um nÚmero entre 1 e 100:")
    chute = int(chute_str)
    rodada = rodada + 1
    print("O número que você digitou é: ", chute)

    if (chute < 1 or chute > 100):
        print("Número inválido. Digite um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O numero que você digitou é maior do que o numero secreto.")
        elif (menor):
            print("Você errou! O numero que você digitou é menor do que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print(pontos)
print("Fim do jogo")

