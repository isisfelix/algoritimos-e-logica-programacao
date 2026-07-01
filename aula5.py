def fatorial(n):
    fat = 1

    for i in range(1, n + 1):
        fat = fat * i

    return fat


n = int(input("Digite um número: "))

while n != 0:
    print("Fatorial =", fatorial(n))

    n = int(input("Digite outro número (0 para sair): "))

print("Fim do programa!")