def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    multiplicador_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_1 = sum(int(cpf[i]) * multiplicador_1[i] for i in range(9))
    resto_1 = soma_1 % 11
    if resto_1 < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - resto_1
    
    multiplicador_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_2 = sum(int(cpf[i]) * multiplicador_2[i] for i in range(10))
    resto_2 = soma_2 % 11
    if resto_2 < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - resto_2
    
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return "Válido"
    else:
        return "Inválido"

cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf))