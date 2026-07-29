from modulos import arquivos


metas = arquivos.carregar_metas() 


def abrir():
    while True:
        print("\n===== MÓDULO DE METAS =====")
        print("1 - Adicionar meta")
        print("2 - Listar metas")       
        print("3 - Remover meta")
        print("4 - Concluir meta")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite a meta: ")
            nova_meta = {
            "nome": nome,
            "concluida": False
            }
            metas.append(nova_meta)
            arquivos.salvar_metas(metas)
            print("\nMeta adicionada com sucesso!")

        elif opcao == "2":
            print("\n===== SUAS METAS =====")
            for numero, meta in enumerate(metas):
                if meta["concluida"]:
                    status = "✅"
                else:
                    status = "⌛"
                print(f"{numero + 1}. {status} {meta['nome']}")

        elif opcao == "3":
            numero = int(input("\nDigite o número da meta: "))   
            removida = metas.pop(numero - 1)
            arquivos.salvar_metas(metas)
            print(f"\nMeta removida com sucesso: {removida['nome']}")

        elif opcao == "4":
            try:
                numero = int(input("\nDigite o número da meta: "))
                metas[numero - 1]["concluida"] = True
                arquivos.salvar_metas(metas)
                print("\nMeta marcada como concluída")

            except ValueError:
                print("\nDigite um número válido.")

            except IndexError:
                print("\nMeta não encontrada")
                
        elif opcao == "0":
            break
        
        else:
            print("\nOpção inválida") 