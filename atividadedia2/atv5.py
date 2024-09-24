import random

opcoes = ["Cara", "Coroa"]

resultados = []

while True:
    resultado = random.choice(opcoes)
    print(f"O resultado do lançamento da moeda é: {resultado}")
    resultados.append(resultado)

    resposta = input("Deseja lançar a moeda novamente? (s/n) ")
    if resposta == "s" or resposta == "S":
        continue
    elif resposta == "n" or resposta == "N":
        break
    else:
        print("Resposta inválida. Por favor, digite 's' ou 'n'.")