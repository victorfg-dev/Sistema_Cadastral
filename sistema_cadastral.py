def main():
    cadastrados = []
    escolha = 0
    while True:
        print("\n\tMENU\n[1] Novo cadastro\t[4] Buscar cadastro\n[2] Deletar cadastro\t[5] Ver cadastros\n[3] Sair")
        escolha = int(input("\nEscolha: "))

        if escolha == 1:
            cadastrar(cadastrados)
        elif escolha == 2:
            deletar(cadastrados)
        elif escolha == 3:
            break
        elif escolha == 4:
            buscar(cadastrados)
        elif escolha == 5:
            print(cadastrados)
        else:
            print("\nEscolha invalida.")
    return(0)
def cadastrar(cadastrados):
    n = int(input("\nInforme o cadastro a ser realizado: "))
    cadastrados.append(n)
    return (cadastrados)
def deletar(cadastrados):
    n = int(input("\nInforme o indice do cadastro a ser removido ou digite -1 para retornar ao Menu: "))
    if n == -1:
        return 0;
    del cadastrados[n]
    return (cadastrados)
def buscar(cadastrados):
    encontrado = False
    n = int(input("Informe o cadastro a ser buscado: "))
    for i in range(len(cadastrados)):
        if cadastrados[i] == n:
            print("Cadastro encontrado no indice: {}".format(i))
            encontrado = True
    
    if not encontrado:
        print("\nCadastro nao encontrado.")
    
    return(0)

main()
