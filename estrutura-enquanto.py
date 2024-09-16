#1ª forma de utilizar while - semelhante ao FOR
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1  # é o mesmo quecontador +=1

    print("="*40)
    #2 forma de utilizar enquanto - loop condicional normal
    valor = 0

    while valor >=0:
        valor = int(input("informe um valor qualquer(digite um valor negativo para terminar)"))

        print(f"você digitou (valor)")

        print("-"*40)

        #1ª forma de utilizar o enquanto - semelhante a estrutura faça...enquanto

        while true:
            senha = input("Informe sua senha: ")

            if senha == "123":
                print("parabéns, senha correta")
                break # forma de encerrar o loop
            else:
                print("Senhas não conferem, tente novamente")