# Inicializa a variável para armazenar o total da compra
total = 0

print("***** Lojão do Manoel *****")

# Loop para inserir os preços dos produtos
contador = 1
while True:
    # Solicita ao usuário o preço do produto
    preco = float(input(f"Produto {contador}: R$"))
    
    # Verifica se o preço é 0, o que indica o fim da entrada
    if preco == 0:
        break
    
    # Adiciona o preço ao total
    total += preco
    contador += 1

# Exibe o total da compra
print(f"Total: R${total:.2f}")

# Solicita o valor em dinheiro do cliente
while True:
    # Solicita ao usuário o valor em dinheiro
    dinheiro = float(input("Dinheiro: R$"))
    
    # Verifica se o dinheiro é suficiente para o pagamento
    if dinheiro < total:
        print("O valor fornecido é menor que o total da compra. Por favor, insira um valor suficiente.")
    else:
        # Calcula o troco
        troco = dinheiro - total
        print(f"Troco: R${troco:.2f}")
        break