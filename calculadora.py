num1 = float(input("Digite o primeiro número aqui: "))
num2 = float(input("Digite o segundo número aqui: "))

print("Menu")

print("""1 - Média ponderada, com pesos 2 e 3
         2 - Quadrado da soma dos dois números
         3 - Cubo do menor número""")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print(f"A média ponderada é {((num1*2)+(num2*3))/(2+3)}")

elif opcao == "2":
    print(f"O quadrado da soma é: {(num1+num2)**2}")

elif opcao == "3":
    if num1<num2: print(f"O cubo do menor número é: {num1**3}")

else: print(f"O cubo do menor número é {num2**3}")
