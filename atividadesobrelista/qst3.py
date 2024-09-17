def main():
    # Solicita ao usuário para inserir 6 números e armazena-os em uma lista
    numeros = []
    print("Digite 6 números:")
    for _ in range(6):
        num = float(input("Número: "))  # Assumimos que a entrada será válida
    
    # Exibe a lista de números
    print("\nLista de números:", numeros)

    # Solicita ao usuário para escolher duas posições
    pos1 = int(input("Escolha a primeira posição (0-5): "))
    pos2 = int(input("Escolha a segunda posição (0-5): "))
    
    # Obtém os números nas posições escolhidas
    num1 = numeros[pos1]
    num2 = numeros[pos2]

    # Calcula e exibe os resultados das operações
    print(f"\nNúmero 1: {num1}")
    print(f"Número 2: {num2}")
    
    print(f"Soma: {num1 + num2}")
    print(f"Produto: {num1 * num2}")
    print(f"Diferença: {num1 - num2}")
    
    # Verifica se a divisão é possível
    if num2 != 0:
        print(f"Divisão: {num1 / num2}")
    else:
        print("Divisão: Não é possível dividir por zero.")
    
    print(f"Exponenciação: {num1 ** num2}")

# Chama a função principal
main()