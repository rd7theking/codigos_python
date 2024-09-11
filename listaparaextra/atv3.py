# Define a média
media = 33.5

# Inicializa contadores
acima_ou_igual = 0
abaixo = 0

# Recebe e processa 7 temperaturas do usuário
print("Digite 7 temperaturas:")

for i in range(7):
    temperatura = float(input(f"Temperatura {i + 1}: "))
    if temperatura >= media:
        acima_ou_igual += 1
    else:
        abaixo += 1

# Exibe os resultados
print(f"Quantidade de temperaturas iguais ou acima da média (33.5): {acima_ou_igual}")
print(f"Quantidade de temperaturas abaixo da média (33.5): {abaixo}")