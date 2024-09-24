def main():
    notas = []
    continuar = True

    print("Digite as notas dos alunos (digite 0 para terminar):")

    while continuar:
        nota = float(input("Nota: "))
        if nota != 0:
            notas.append(nota)
        else:
            continuar = False  # Encerra o loop se a nota for zero

    # Contando quantos alunos ficaram acima da média
    media = 7
    acima_da_media = sum(1 for nota in notas if nota > media)

    print(f"Quantidade de alunos com notas acima da média: {acima_da_media}")

if __name__ == "__main__":
    main()