# Inicializa variáveis para contagem e soma
negative_count = 0
positive_sum = 0

# Recebe 8 números do usuário
print("Digite 8 números:")

for _ in range(8):
    num = float(input("Digite um número: "))
    if num < 0:
        negative_count += 1
    else:
        positive_sum += num

# Exibe os resultados
print(f"Quantidade de números negativos: {negative_count}")
print(f"Soma dos números positivos: {positive_sum}")