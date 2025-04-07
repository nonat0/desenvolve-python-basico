import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'\d', senha):
        return False
    if not re.search(r'[@#$%^&*!]', senha):
        return False
    return True

# Loop para entrada do usuário
while True:
    senha = input("Digite uma senha (ou 'fim' para sair): ")
    if senha.lower() == 'fim':
        break
    if validador_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida! Certifique-se de atender a todos os critérios.")
