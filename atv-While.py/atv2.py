import datetime

ano_atual = datetime.date.today().year

while True:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    
    if idade >= 18:
        print("Inscrição realizada com sucesso!")
        break
    else:
        print("Você precisa ter 18 anos ou mais para se inscrever. Tente novamente.")