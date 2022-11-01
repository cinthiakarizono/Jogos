print("#############################################")
print("Olá! Seja bem vindo ao jogo de adivinhação!")
print("#############################################")

numero_secreto = 42
rodada = 1
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    print("Tentativa ", rodada, "de ", total_de_tentativas)
    chute_str = input("Digite um numero entre 1 e 100:")
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
    print("Fim do jogo")

