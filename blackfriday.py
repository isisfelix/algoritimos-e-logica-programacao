valor = float(input("Dígite o valor total da compra:"))
print("Descontos")

print("""      1 - A vista (15% de desconto)
      2- Cartão de Débito (10% de desconto)
      3- Cartão de Crédito (5% de desconto)""")
desconto = input("Dígite qual opção deseja: ")

if desconto == "1":
     print(f"O valor final à vista foi de: {valor-(valor*0.15):.2f}")

elif desconto == "2":
     print(f"O valor final no cartão de débito foi de: {valor-(valor*0.10):.2f}")

elif desconto == "3":
     print(f"O valor final no cartão de crédito foi de: {valor-(valor*0.05):.2f}")

else:
     print("Não temos esta opção disponivel")