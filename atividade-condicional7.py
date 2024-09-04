valor_produto = float(input("Digite o valor do produto: "))
opcao_pagamento = int(input("Digite o código da condição de pagamento: "))

if opcao_pagamento == 1: 
    desconto = 0.15
    valor_final = valor_produto*(1-desconto)
    
elif opcao_pagamento == 2: 
    desconto = 0.10
    valor_final = valor_produto*(1-desconto)
    
elif opcao_pagamento == 3: 
    desconto = 0
    valor_final = valor_produto*(1-desconto)
    
elif opcao_pagamento == 4:
    juros = 0.10  
    valor_final = valor_produto*(1+juros)

else:
    print("Opção de pagamento inválida!")

print(f"Valor original:R$ {valor_produto: .2f}")
print(f"Código de pagamento: {opcao_pagamento}")
print(f"Valor final: R${valor_final: .2f}")