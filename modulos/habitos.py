from modulos import arquivos

habitos = arquivos.carregar_habitos()


def abrir():
    while True:
        print("\n===== MÓDULO DE HÁBITOS =====")
        print("1 - Adicionar hábito")
        print("2 - Listar hábitos")
        print("3 - Remover hábito")
        print("4 - Marcar hábito como realizado hoje")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite o hábito: ")
            novo_habito = {
                "nome": nome,
                "concluido_hoje": False
            }
            habitos.append(novo_habito)
            arquivos.salvar_habitos(habitos)
            print("\nHábito adicionado com sucesso!")

        elif opcao == "2":
            print("\n===== SEUS HÁBITOS =====")
            for numero, habito in enumerate(habitos):
                if habito["concluido_hoje"]:
                    status = "✅"
                else:
                    status = "⌛"
                print(f"{numero + 1}. {status} {habito['nome']}")

        elif opcao == "3":
            numero = int(input("\nDigite o número do hábito: "))
            removido = habitos.pop(numero - 1)
            arquivos.salvar_habitos(habitos)
            print(f"\nHábito removido com sucesso: {removido['nome']}")

        elif opcao == "4":
            numero = int(input("\nDigite o número do hábito: "))
            habitos[numero - 1]["concluido_hoje"] = True
            arquivos.salvar_habitos(habitos)
            print("\nHábito marcado como realizado hoje")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida") 