numeros = []

print("Digite pelo menos 4 numeros inteiros. Para concluir, digite 'ok'")

while True:
    entrada = input("Digite um número inteiro: ")
    
    if entrada.lower() == 'ok':
        if len(numeros) >= 4:
            break
        else:
            print ("você precisa digitar pelo menos 4 números.")
            continue
    
    try:
        numeros.append(int(entrada))
    except ValuError:
        print("Número ou caracteres inválidos. Por favor, digite novamente. ")
        
par = [num for num in numeros if num % 2 ==0]
impar = [num for num in numeros if num % 2 !=0]
        
print("\nLista original:", numeros)
print("Os 3 primeiros elementos", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida", numeros[::-1])
print("Elementos de índice par:", par)
print("Elementos de índice ímpar:", impar)