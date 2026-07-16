tarefas = []

def abrir():
    while True:    
        print("===== MÓDULO DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefa")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
           nome = input("\nDigite a tarefa: ")
           tarefas.append(nome)
           print("\nTarefa adicionada com sucesso!")

        elif opcao == "2":
           print("\n ===== SUAS TAREFAS =====")
           
           for numero, tarefa in enumerate(tarefas):
              print(f"{numero + 1}. {tarefa}")

        elif opcao == "0":
          break 
        