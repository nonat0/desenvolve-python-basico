import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) > 3:
            meio = list(palavra[1:-1]) 
            random.shuffle(meio)  
            return palavra[0] + ''.join(meio) + palavra[-1] 
        return palavra  
    
    palavras = frase.split() 
    palavras_embaralhadas = [embaralhar_palavra(p) for p in palavras] 
    return ' '.join(palavras_embaralhadas) 


while True:
    frase = input("Digite uma frase (ou 'fim' para sair): ")
    if frase.lower() == "fim":
        break
    resultado = embaralhar_palavras(frase)
    print(resultado)
