def main():
    # Solicita ao usuário para preencher a lista com 10 números inteiros
    lista = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        num = int(input(f"Número {i+1}: "))
        lista.append(num)
    
    # Exibe a lista
    print("\nLista de números:", lista)

    # Verifica a existência do número 3 e mostra as posições
    posicoes = [i for i, valor in enumerate(lista) if valor == 3]
    
    if posicoes:
        print("nO número 3 aparece nas seguintes posições:", posicoes)
    else:
        print("\O número 3 não foi encontrado na lista.")

# Chama a função principal
main()