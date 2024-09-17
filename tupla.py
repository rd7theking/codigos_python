objetos = ('lapis', 'borracha', 'caderno') 
print(objetos[1]) #Irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos))# irá mostrar o tipo de variável

print(objetos) #exibindo todos os itens de uma só vez

print("-"*50)
for item in range(0,3):
    print(objetos[item], end=", ")# exibindo todos os itens da tupla

    # Exibindo todos os itens da tupla sem a finção range
    print("")
    print("-"*50)
    for elementos in objetos:
        print(elementos)

        # Iremos tentar alterar o conteúdo da tupla
        objetos[0] = "caneta"