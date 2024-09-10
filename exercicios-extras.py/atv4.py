def calcular_imposto(salario):
    if salario <= 1900:
        return 0  # Isento de imposto
    elif 1901 <= salario <= 2800:
        return salario * 0.075
    elif 2801 <= salario <= 3700:
        return salario * 0.15
    else:
        return salario * 0.225

# Solicita o salário ao usuário
try:
    salario = float(input("Digite o salário do funcionário: R$ "))
    if salario < 0:
        print("Salário inválido. Por favor, digite um valor positivo.")
    else:
        imposto = calcular_imposto(salario)
        print(f"O imposto de renda devido é: R$ {imposto:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para o salário.")
