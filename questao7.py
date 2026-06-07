import random

numero_sorteado = random.randint(1, 10)

for tentativa in range(1, 4):
    palpite = int(input("Digite um número de 1 a 10: "))

    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        break

    else:
        print("Você errou!")

        if palpite < numero_sorteado:
            print("Tente um número maior")
        else:
            print("Tente um número menor")

        if tentativa == 3:
            print("Você perdeu!")
            print("O número era:", numero_sorteado)