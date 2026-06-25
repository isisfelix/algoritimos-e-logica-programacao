usuário = []
senha = []
print("Digite encerrar no usuario ou na senha para finalizar.")
while True:
    cadastro_usu = input("Cadastre seu usuário aqui: ")
    if cadastro_usu.lower() == "encerrar":
        break
    cad_senha = input("Cadastre sua senha aqui: ")
    if cad_senha.lower() == "encerrar":
        break
    usuário.append(cadastro_usu)
    senha.append(cad_senha)
    print("Cadastro concluido!")

login_usu = input("Dígite seu usuário aqui: ")
login_senha = input("Dígite sua senha aqui: ")
if login_usu in usuário:
    indice = usuário.index(login_usu)
    if login_senha == senha[indice]:
        print(f"Bem vindo, {login_usu}!")
    else: print("Senha errada!")
else: print("Usuário invalido!")