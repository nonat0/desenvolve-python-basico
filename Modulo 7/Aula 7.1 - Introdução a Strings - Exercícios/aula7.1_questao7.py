   for nome in nomes:
        nome_cripto = "".join(
            chr(((ord(c) - 33 + n) % 94) + 33) for c in nome) 
        nomes_cript.append(nome_cripto)
    
    return nomes_cript, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)
print("Chave de criptografia:", chave)
print("Nomes criptografados:", nomes_cript)
