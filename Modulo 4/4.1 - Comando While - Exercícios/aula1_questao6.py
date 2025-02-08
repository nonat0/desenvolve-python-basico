N = int(input("Digite a quantidade de experimentos registrados: "))

total_sapos = 0
total_ratos = 0
total_coelhos = 0

for _ in range(N):
    entrada = input("Digite a quantidade e o tipo de cobaia (ex: 10 C): ").split()
    quantia = int(entrada[0]) 
    tipo = entrada[1].upper()  

    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

total_cobaias = total_sapos + total_ratos + total_coelhos

percent_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percent_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percent_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

print("\nRELATÓRIO FINAL:")
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")