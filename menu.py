from modulos import (
    habitos, 
    tarefas,
    metas,
)

def mostrar_menu():
    print("====================")
    print("       LifeOS")
    print("====================")
    print()
    print("1 - Tarefas")
    print("2 - Hábitos")
    print("3 - Metas")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")
    return opcao

def executar_menu():
    while True:
         opcao = mostrar_menu()

         if opcao == "1":
             tarefas.abrir()

         elif opcao == "2":
            habitos.abrir()
    
         elif opcao == "3":
            metas.abrir()

         elif opcao == "0":
            print("\nAté logo!")

         else:
            print("\nOpção Inválida!")