def calcular_valores_compra(valor_compra, parcelas):
    # Verifica se o número de parcelas está entre 1 e 24
    if parcelas < 1 or parcelas > 24:
        return "Número de parcelas deve ser entre 1 e 24."

    # Aplica os juros e custos adicionais
    valor_total = valor_compra
    if parcelas > 12:
        # Aplica juros de 1,5%
        valor_total *= 1.015
        
        # Adiciona R$6 para cada parcela além da 12ª
        parcelas_adicionais = parcelas - 12
        valor_total += parcelas_adicionais * 6

    # Calcula o valor de cada parcela
    valor_parcela = valor_total / parcelas

    return valor_total, valor_parcela

# Recebe entrada do usuário
try:
    valor_compra = float(input("Digite o valor da compra: R$ "))
    parcelas = int(input("Digite a quantidade de parcelas (1 a 24): "))
    
    # Calcula valores
    resultado = calcular_valores_compra(valor_compra, parcelas)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        valor_total, valor_parcela = resultado
        print(f"\nValor total a ser pago: R$ {valor_total:.2f}")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, insira valores numéricos.")