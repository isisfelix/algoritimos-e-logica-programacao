import random
print("-"*50)
print("Rifa")
print("Dígite encerrar para finalizar a rifa")
print("-"*50)
parti = []
while True:
    pessoas = str(input("Dígite o nome do comprador: "))
    if pessoas.lower() == "encerrar":
        break
    parti.append(pessoas)
vence = random.choice(parti)
print("Encerrando a Rifa")
print(f"O vencedor da rifa é {vence}")