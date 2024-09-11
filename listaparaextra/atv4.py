# Inicializa uma lista para armazenar os números
numeros = []

# Recebe 5 números inteiros do usuário
print("Digite 5 números inteiros:")

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Encontra o maior número na lista
maior_numero = max(numeros)

# Exibe o maior número
print(f"O maior número informado é: {maior_numero}")