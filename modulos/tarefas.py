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

        opcao = input("\nEscolha uma opção: ")

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
            print("\n===== SUAS TAREFAS =====")
            for numero, tarefa in enumerate(tarefas):
                if tarefa["concluida"]:
                    status = "✅"
                else:
                    status = "⏳"
                print(f"{numero + 1}. {status} {tarefa['nome']}")

        elif opcao == "3":

            if not tarefas:
                print("\nNenhuma tarefa cadastrada.")
                continue

            try:
                numero = int(input("\nDigite o número da tarefa que deseja remover: "))
                removida = tarefas.pop(numero - 1)
                arquivos.salvar_tarefas(tarefas)
                print(f"\nTarefa removida: {removida['nome']}")

            except ValueError:
                print("\nDigite um número válido.")

            except IndexError:
                print("\nTarefa não encontrada.")

        elif opcao == "4":

            if not tarefas:
                print("\nNenhuma tarefa cadastrada.")
                continue

            try:
                numero = int(input("\nDigite o número da tarefa que deseja concluir: "))

                if numero < 1:
                    print("\nTarefa não encontrada.")
                    continue

                tarefas[numero - 1]["concluida"] = True
                arquivos.salvar_tarefas(tarefas)
                print("\nTarefa marcada como concluída")

            except ValueError:
                print("\nDigite um número válido.")

            except IndexError:
                print("\nTarefa não encontrada.")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida")
        