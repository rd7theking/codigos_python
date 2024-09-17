# Coleta valores até que um valor negativo seja digitado
valores = []
valor = 0  # Inicializa a variável com um valor não-negativo para iniciar o loop

while valor >= 0:
    valor = int(input("Digite um valor (ou um número negativo para encerrar): "))
    if valor >= 0:
        valores.append(valor)

# Remove números pares da lista
valores = [num for num in valores if num % 2 != 0]

# Exibe a lista criada e a lista sem números pares
print("Lista criada:", valores)