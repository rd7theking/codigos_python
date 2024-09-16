import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Número máximo de tentativas
tentativas_restantes = 5

print("Bem-vindo ao jogo da adivinhação!")
print("Eu escolhi um número entre 1 e 100.")
print("Você tem 5 tentativas para adivinhar qual é o número.")

# Variável de controle para encerrar o loop
acertou = False

# Loop principal do jogo
while tentativas_restantes > 0:
    # Solicita ao usuário um palpite
    palpite = int(input("Digite seu palpite: "))
    
    # Verifica se o palpite é o número secreto
    if palpite == numero_secreto:
        acertou = True
        print("Parabéns! Você acertou o número!")
        break  # Termina o loop se o número foi acertado
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
    
    # Reduz o número de tentativas restantes
    tentativas_restantes -= 1
    print(f"Tentativas restantes: {tentativas_restantes}")

# Mensagem final se o usuário não acertar o número
if acertou:
    print("Você acertou o número antes de usar todas as tentativas.")
else:
    print(f"Você usou todas as tentativas. O número secreto era {numero_secreto}.")