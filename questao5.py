a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a < b:
    soma = 0

    for i in range(a, b + 1):
        soma += i

    print("A soma é:", soma)
else:
    print("Erro: a deve ser menor que b.")