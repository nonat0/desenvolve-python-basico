frase = input("Digite uma frase: ")
soma=0
for i in range(len(frase)):
    if frase[i] == " ":
        soma+=1

print("Espaços em branco: ", soma)