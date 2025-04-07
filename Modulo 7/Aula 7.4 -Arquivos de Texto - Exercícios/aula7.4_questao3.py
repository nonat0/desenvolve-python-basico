import re

with open("estomago.txt", "r", encoding="latin-1") as f:
    linhas = f.readlines()

print("".join(linhas[:25]))
print(len(linhas))
linha_maior = max(linhas, key=len)
print(linha_maior.strip())

texto = " ".join(linhas)
nonato = len(re.findall(r'\bnonato\b', texto, flags=re.IGNORECASE))
iria = len(re.findall(r'\bíria\b', texto, flags=re.IGNORECASE))
print(f"Menções a Nonato: {nonato}")
print(f"Menções a Íria: {iria}")