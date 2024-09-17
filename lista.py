animais = ["coelho", "gato", "ovelha"]
print(type(animais))#exibindo o tipo de variável

print(animais)

#Exibindo todos os itens da lista
print("-"*50)
for itens in animais:
    print("-"*50)
    animais[0] = "coelho"
    print(animais)

    #2ª Etapa: inserir dados
    print("-"*50)
    animais.append("cavalo")#irá inserir um novo item no final da lista
    print(animais)

    #2ª forma - usando insert
    animais.insert(1, "ovelha")# o insert precisa de 2 valores, o 1° será o indice que desejo inserir o valor. o 2° é o conteudo que quero inserir na lista  
    print(animais)

    #3ª Etapa: excluir dados
    print("-"*50)
    #Forma 3 - usando pop()
    animais.pop()#Remove o último item da lista
    print(animais)

    #Forma 2 - Usando pop() com indice
    animais.pop(0)# Aqui iremos escolher qual indice da lista será excluido
    print(animais)

    #Forma 3 - Usando remove
    animais.remove("ovelha")#Irá resolver o item pelo seu conteúdo
    print(animais)