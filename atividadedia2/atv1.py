def obter_lista(mensagem):
    lista = input(mensagem).split()
    return [int(num) for num in lista]

# Lê as duas listas
lista1 = obter_lista("Digite a primeira lista de números inteiros, separados por espaço: ")
lista2 = obter_lista("Digite a segunda lista de números inteiros, separados por espaço: ")

# Converte as listas em conjuntos e encontra a interseção
intersecao = set(lista1).intersection(set(lista2))

# Ordena a interseção em ordem crescente
resultado = sorted(intersecao)

# Exibe o resultado
print("Números comuns em ordem crescente:", resultado)