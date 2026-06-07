num1 = int(input("Digite o primeiro termo: "))
quant = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

for i in range(quant):
    termo = num1 + i * razao
    print(termo)