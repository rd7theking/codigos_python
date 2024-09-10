def is_bissexto(ano):
    # Verifica se o ano é bissexto
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

# Solicita um ano ao usuário
try:
    ano = int(input("Digite um ano: "))
    if is_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido.")