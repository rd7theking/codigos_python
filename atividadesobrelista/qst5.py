def main():
    # Solicita ao usuário para preencher a lista com 5 números inteiros
    numeros = []
    print("Digite 5 números inteiros:")
    for i in range(5):
        num = int(input(f"Número {i+1}: "))
        numeros.append(num)
    
    # Exibe a lista completa
    print("\nLista completa:", numeros)

    # Filtra e exibe os números divisíveis por 3
    divisiveis_por_3 = [num for num in numeros if num % 3 == 0]
    print("\Valores divisíveis por 3:", divisiveis_por_3)

# Chama a função principal
main()