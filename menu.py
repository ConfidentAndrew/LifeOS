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

         print(f"Você escolheu: {opcao}")