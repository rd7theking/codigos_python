def calcular_salario(horas_trabalhadas, valor_por_hora):
    # Define o limite de horas normais
    HORAS_NORMAIS = 40
    
    if horas_trabalhadas <= HORAS_NORMAIS:
        # Salário normal se horas trabalhadas forem 40 ou menos
        salario = horas_trabalhadas * valor_por_hora
    else:
        # Calcula o salário para horas normais
        salario_normal = HORAS_NORMAIS * valor_por_hora
        # Calcula as horas extras
        horas_extras = horas_trabalhadas - HORAS_NORMAIS
        # Calcula o valor das horas extras com 50% de bônus
        salario_horas_extras = horas_extras * valor_por_hora * 1.5
        # Total do salário
        salario = salario_normal + salario_horas_extras
    
    return salario

# Solicita ao usuário a quantidade de horas trabalhadas e o valor por hora
try:
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
    valor_por_hora = float(input("Digite o valor por hora: R$ "))
    
    if horas_trabalhadas < 0 or valor_por_hora < 0:
        print("Valor inválido. Horas trabalhadas e valor por hora devem ser não negativos.")
    else:
        salario = calcular_salario(horas_trabalhadas, valor_por_hora)
        print(f"O salário total é: R$ {salario:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos válidos.")
