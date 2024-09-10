def verificar_faixa(numero):
    if 0 <= numero <= 25:
        return "O número está na faixa de 0 a 25."
    elif 26 <= numero <= 50:
        return "O número está na faixa de 26 a 50."
    elif 51 <= numero <= 75:
        return "O número está na faixa de 51 a 75."
    elif 76 <= numero <= 100:
        return "O número está na faixa de 76 a 100."
    else:
        return "Número fora do intervalo permitido. Digite um número entre 0 e 100."

# Solicita um número ao usuário
try:
    numero = int(input("Digite um número de 0 a 100: "))
    print(verificar_faixa(numero))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
