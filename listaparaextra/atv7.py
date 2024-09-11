# Solicita dois números inteiros positivos ao usuário
a = int(input("Digite o número inteiro positivo a: "))
b = int(input("Digite o número inteiro positivo b: "))

# Garante que a seja menor ou igual a b
if a > b:
    a, b = b, a  # Troca os valores para garantir a <= b

# Inicializa a contagem de números múltiplos de 7 e 11 (ou seja, múltiplos de 77)
contagem = 0

# Percorre a faixa de números entre a e b
for numero in range(a, b + 1):
    if numero % 77 == 0:
        contagem += 1

# Exibe o resultado final
print(f"O total de números entre {a} e {b} que são múltiplos de 7 e 11 simultaneamente é: {contagem}")
