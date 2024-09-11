def verificar_numero_perfeito(n):
    # Cria uma lista para armazenar os divisores próprios
    divisores = [divisor for divisor in range(1, n) if n % divisor == 0]
    # Calcula a soma dos divisores próprios
    soma_divisores = sum(divisores)
    # Verifica se a soma dos divisores é igual ao número e imprime a mensagem correspondente
    if soma_divisores == n:
        print(f"O número {n} é um número perfeito.")
    else:
        print(f"O número {n} não é um número perfeito.")

# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para verificar se o número é perfeito e exibe a mensagem
verificar_numero_perfeito(numero)