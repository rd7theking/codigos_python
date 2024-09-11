import random

# Inicializa um dicionário para armazenar a contagem das ocorrências de cada valor
contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simula 10 lançamentos de dados
for _ in range(10):
    numero_sorteado = random.randint(1, 6)  # Sorteia um número entre 1 e 6
    contagem[numero_sorteado] += 1  # Atualiza a contagem do número sorteado

# Exibe a contagem de cada valor
print("Contagem dos valores sorteados:")
for valor, quantidade in contagem.items():
    print(f"Valor {valor}: {quantidade} vez(es)")