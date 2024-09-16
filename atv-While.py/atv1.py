numero = 0
while numero >= 0:
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 0:
        print("Programa encerrado.")
    elif numero > 100:
        print("Limite excedido")
    elif numero > 10:
        print(f"O quadrado de {numero} é {numero ** 2}")
    elif numero > 5:
        print(f"O cubo de {numero} é {numero ** 3}")
    else:
        print(f"Valor digitado: {numero}")

