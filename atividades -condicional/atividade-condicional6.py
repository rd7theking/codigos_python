A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

valores = [A,B,C]
valores.sort(reverse=True)

print(f"Os valores em ordem decrescente são: {valores}")