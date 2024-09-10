

def verificar_aprovacao(nota, frequencia):
    # Verifica se o aluno é aprovado ou reprovado
    if nota >= 7 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"

# Recebe a nota final e a frequência do aluno
try:
    nota = float(input("Digite a nota final do aluno: "))
    frequencia = float(input("Digite a frequência do aluno em %: "))
    
    # Verifica a aprovação
    resultado = verificar_aprovacao(nota, frequencia)
    
    print(f"O aluno está: {resultado}")

except ValueError:
    print("Entrada inválida. Por favor, insira valores numéricos para a nota e a frequência.")
