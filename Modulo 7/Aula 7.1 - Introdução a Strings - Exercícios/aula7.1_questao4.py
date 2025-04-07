numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero

if len(numero) == 9 and numero[0] == "9":
    numero_formatado = numero[:5] + "-" + numero[5:]
    print("Número completo:", numero_formatado)
else:
    print("Número inválido.")