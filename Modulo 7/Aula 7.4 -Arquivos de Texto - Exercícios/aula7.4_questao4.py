import random

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()

palavra = random.choice(palavras).lower()
resposta = ["_"] * len(palavra)

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().split("-----\n")

tentativas = 6
erros = 0
letras_usadas = []

while erros < tentativas and "_" in resposta:
    print(" ".join(resposta))
    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                resposta[i] = letra
    else:
        imprime_enforcado(erros, estagios)
        erros += 1

if "_" not in resposta:
    print("Parabéns! Você acertou: " + palavra)
else:
    imprime_enforcado(erros - 1, estagios)
    print("Você perdeu! A palavra era: " + palavra)