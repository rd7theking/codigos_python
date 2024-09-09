nome = input("Digite o nome ")
sexo = input("Digite o sexo (M/F:) ")
estado_civil = input("Digite o estado civil(solteiro/casado): ")

if sexo == "F" and estado_civil == "casada": 
    tempo_casada = int(input("Digite o tempo de casada (anos): "))
    print(f"{nome}, você é casada há {tempo_casada}anos: ")
else:
    print(f"{nome},obrigado e até a próxima!")
    