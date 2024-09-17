meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = [float(input(f"Digite a temperatura média para {m}: ")) for m in meses]

for m, t in zip(meses, temperaturas):
    if t > sum(temperaturas) / len(temperaturas):
        print(f"{m}: {t:.2f}°C")