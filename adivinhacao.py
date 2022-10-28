print("#############################################")
print("Olá! Seja bemm vindo ao jogo de adivinhação!")
print("#############################################")

numero_secreto = 42
chute = input("Digite um numero:")

if (chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")
