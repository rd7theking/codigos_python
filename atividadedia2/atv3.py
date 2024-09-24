def exibir_eventos(eventos):
    print("\nEventos agendados para o mês:")
    for evento in eventos:
        print(evento)
    print()

def main():
    eventos = [
        "reunião com a equipe",
        "almoço com cliente",
        "consulta médica"
    ]

    while True:
        exibir_eventos(eventos)

        print("Menu de gerenciamento de eventos")
        print("1. Adicionar um novo evento")
        print("2. Remover um evento")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == "1":
            novo_evento = input("Digite o novo evento: ")
            eventos.append(novo_evento)
        elif escolha == "2":
            posicao = int(input("Qual a posição do evento? ")) - 1
            if 0 <= posicao < len(eventos):
                eventos.pop(posicao)
                print("Evento removido com sucesso!")
            else:
                print("Posição inválida.")
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()