from lib.crud import (Cadastrar, Consultar, Editar, Deletar)
from time import sleep


# exibição do menu e chamada de funções
def mainMenu():
    option = -1
    while(option != 0):
        print("-=-"*11, "\n|  [1] Cadastrar  | [3] Editar  |\n|  [2] Consultar  | [4] Deletar |\n", "-=-"*11)
        
        # Verificação das entradas
        while True:
            try:
                 option = int(input("\nDigite 0 para sair.\nEscolha: "))
            except:
                 print("Opção inválida.")
                 sleep(2)
                 
            
            if (option > 4 or option < 0):
                print("Opção inválida.")
                sleep(2)
            else:
                break
        
        # chamada de funções
        if (option == 1):
            Cadastrar()
        elif (option == 2):
            Consultar()
        elif (option == 3):
            Editar()
        elif (option == 4):
            Deletar()

mainMenu()