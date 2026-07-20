from modulos import arquivos


tarefas = arquivos.carregar_tarefas()


def abrir():
    while True:    
        print("===== MÓDULO DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefa")
        print("3 - Remover tarefa")
        print("4 - Concluir tarefa")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
           nome = input("\nDigite a tarefa: ")
           tarefa = {
              "nome": nome,
              "concluida": False
           }
           tarefas.append(tarefa)
           arquivos.salvar_tarefas(tarefas)
           print("\nTarefa adicionada com sucesso!")

        elif opcao == "2":
           print("\n ===== SUAS TAREFAS =====")           
           for numero, tarefa in enumerate(tarefas):
              print(f"{numero + 1}. {tarefa['nome']}")

        elif opcao == "3":
             try:
                numero = int(input("\nDigite o número da tarefa que deseja remover: "))            
                removida = tarefas.pop(numero - 1)
                arquivos.salvar_tarefas(tarefas)
                print(f"\nTarefa removida: {removida}")
             except:
                print("\nNão foi possível remover essa tarefa.")

        elif opcao == "4":
           numero = int(input("\nDigite o número da tarefa concluída: "))
           tarefa = tarefas[numero - 1]
           tarefa["concluida"] = True
           arquivos.salvar_tarefas(tarefas)
           print("\nTarefa concluída com sucesso!")
           
        elif opcao == "0":
          break 
        