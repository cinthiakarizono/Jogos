print("#############################################")
print("Olá! Seja bemm vindo ao jogo de adivinhação!")
print("#############################################")

numero_secreto = 42
rodada = 1
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    print("Tentativa ", rodada, "de ", total_de_tentativas)
    chute_str = input("Digite um numero:")
    chute = int(chute_str)
    print("O numero que você digitou é: ", chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    rodada = rodada + 1

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        print("Você errou! O numero que você digitou é maior do que o numero secreto.")
    elif (menor):
        print("Você errou! O numero que você digitou é menor do que o numero secreto.")
print("Fim do jogo")

