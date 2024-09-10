def classificar_idade(idade):
    # Classifica a idade de acordo com as faixas etárias fornecidas
    if idade < 12:
        return "Criança"
    elif 12 <= idade < 18:
        return "Adolescente"
    elif 18 <= idade <= 60:
        return "Adulto"
    elif idade > 60:
        return "Idoso"
    else:
        return "Idade inválida"

# Solicita a idade ao usuário
try:
    idade = int(input("Digite a idade: "))
    # Verifica se a idade é não negativa
    if idade < 0:
        print("Idade inválida. Por favor, digite uma idade não negativa.")
    else:
        print(f"A pessoa é: {classificar_idade(idade)}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
