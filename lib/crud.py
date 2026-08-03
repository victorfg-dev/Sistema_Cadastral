import json
from time import sleep

# Funções auxiliares
def ler_json():
    with open("users.json", "r", encoding="utf-8") as arquivo:
        return(json.load(arquivo))

def salvar_json(data):
    with open("users.json", "w", encoding="utf-8") as arquivo:
        return json.dump(data, arquivo, indent=4, ensure_ascii=False)




# Insere um novo cadastro no sistema
def Cadastrar():

    data = ler_json()

    # validação de entradas
    while True:

        try:
            nome = str(input("\nInforme o nome completo: "))
            idade = int(input("\nInforme a idade: "))
            codigo = int(input("\nInforme o código: "))
            break
        except:
            print("\nENTRADA INVÁLIDA")
            sleep(2)
    
    user = {
        "nome" : nome,
        "idade" : idade,
        "codigo" : codigo
    }
    data.append(user)
    salvar_json(data)

    repeat = str(input("\nPressione \"Enter\" para  um novo cadastro ou \"S\" para sair.")).strip().upper()
    if (repeat == "S"):
        return
    else:
        Cadastrar()

# Consulta um indice e mostra os dados presentes nele
def Consultar():
    data = ler_json()
    while True:

        try:
            n = int(input("Consultar por:\n[1] Codigo\t[2] Nome\nEscolha: "))
            break
        except:
            print("\nEntrada inválida")
            sleep(2)
        
        if n > 2 or n < 1:
            print("\nEntrada inválida")
            sleep(2)

    if n == 1:

        i = 0
        found = False
        x = int(input("\nInforme o codigo: "))
        
        for user in data:
            if user["codigo"] == x:
                found = True
                print(f"\nO código {x} pertence ao usuário {user["nome"]} de índice {i}")
            i += 1
        
        if not found:
            print("\nCódigo não encontrado.")
    
    if n == 2:

        i = 0
        found = False
        y = str(input("\nInforme o nome: "))

        for user in data:
            if user["nome"] == y:
                found = True
                print(f"\nUsuário encontrado no índice {i}. Código do usuário: {user["codigo"]}")
            i += 1
        
        if not found:
            print("\nUsuário não encontrado")

# Consulta um código e altera os dados presentes do usuário
def Editar():

    data = ler_json()

    try:
        codigo = int(input("\nInforme o código do usuário que deseja editar: "))
    except ValueError:
        print("\nEntrada inválida.")
        return

    found = False

    for user in data:

        if user["codigo"] == codigo:
            found = True

            print(f"Nome atual: {user['nome']}")
            print(f"Idade atual: {user['idade']}")
            print(f"Código atual: {user['codigo']}")

            novo_nome = input("\nNovo nome (Enter para manter): ").strip()
            nova_idade = input("Nova idade (Enter para manter): ").strip()
            novo_codigo = input("Novo código (Enter para manter): ").strip()

            if novo_nome != "":
                user["nome"] = novo_nome

            if nova_idade != "":
                user["idade"] = int(nova_idade)

            if novo_codigo != "":
                user["codigo"] = int(novo_codigo)

            salvar_json(data)

            print("\nUsuário atualizado com sucesso!")
            return

    if not found:
        print("\nCódigo não encontrado.")

# Consulta um indice e remove todos os dados presentes nele
def Deletar():
    data = ler_json()
    while True:

        try:
            n = int(input("\nInforme o código do usuário a ser deletado: "))
            break
        except:
            print("\nEntrada inválida")
            sleep(2)
        
    found = False

    for user in data:
        if user["codigo"] == n:
            found = True
            
            print(f"Nome: {user['nome']}")
            print(f"Idade: {user['idade']}")
            print(f"Código: {user['codigo']}")

            confirm = str(input("\nDeseja deletar esse usuário? [S/N]: ")).upper().strip()

            if confirm != "N" and confirm != "S":
                print("\nEntrada inválida.")
            elif confirm == "N":
                print("\nOperação cancelada.")
                break
            else:
                data.remove(user)
                salvar_json(data)

                print("\nUsuário deletado com sucesso.")
            

    if not found:
        print("\nCódigo não encontrado.")   

    
