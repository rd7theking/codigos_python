import random

def escolher_lista():
    print("Escolha uma lista de palavras:")
    print("1. Animais")
    print("2. Frutas")
    print("3. Países")
    print("4. Cores")
    print("5. Esportes")

    escolha = input("Digite o número da sua escolha: ")

    if escolha == "1":
        return [
            'leão', 'tigre', 'elefante', 'girafa', 'zebra', 
            'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 
            'urso', 'coelho', 'cavalo', 'pinguim', 'lobo'
        ]
    elif escolha == "2":
        return [
            'maçã', 'banana', 'laranja', 'morango', 'uva', 
            'abacaxi', 'kiwi', 'manga', 'pera', 'melancia', 
            'framboesa', 'nectarina', 'carambola', 'figo', 'amora'
        ]
    elif escolha == "3":
        return [
            'Brasil', 'Canadá', 'Japão', 'Austrália', 'França', 
            'Índia', 'México', 'Itália', 'Egito', 'Argentina', 
            'Alemanha', 'China', 'Reino Unido', 'Noruega'
        ]
    elif escolha == "4":
        return [
            'vermelho', 'azul', 'verde', 'amarelo', 'laranja', 
            'roxo', 'rosa', 'marrom', 'preto', 'branco', 
            'cinza', 'turquesa', 'bege', 'lilás', 'prata'
        ]
    elif escolha == "5":
        return [
            'futebol', 'basquete', 'natação', 'tênis', 'vôlei', 
            'corrida', 'rugby', 'golfe', 'ciclismo', 'boxe', 
            'esgrima', 'handebol', 'karate', 'skate', 'surfe'
        ]
    else:
        print("Escolha inválida. Usando a lista de animais por padrão.")
        return [
            'leão', 'tigre', 'elefante', 'girafa', 'zebra', 
            'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 
            'urso', 'coelho', 'cavalo', 'pinguim', 'lobo'
        ]

def main():
    palavras = escolher_lista()
    
    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras)
    posicao_palavra = palavras.index(palavra_secreta)

    print("Bem-vindo ao jogo de adivinhação de palavras!")
    print("Você deve adivinhar a posição da palavra escolhida.")
    print("A lista começa com a posição 0 e vai até 14 (a lista possui 15 itens).")
    
    tentativas = 3

    while tentativas > 0:
        try:
            palpite = int(input(f"\nQual a posição da palavra '{palavra_secreta}'? (Tentativas restantes: {tentativas}): "))
            if palpite < 0 or palpite > 14:
                print("Por favor, insira um número entre 0 e 14.")
                continue
            if palpite == posicao_palavra:
                print("Parabéns! Você acertou a posição da palavra!")
            else:
                tentativas -= 1
                print(f"Você errou! Tentativas restantes: {tentativas}")
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"A posição correta era {posicao_palavra}.")

if __name__ == "__main__":
    main()