def data_por_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    dia, mes, ano = data.split('/')
    mes_extenso = meses[int(mes) - 1]
    
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}. "
data_nascimento = input("Digite sua data de nascimento no formato (dd/mm/aaa):")
print(data_por_extenso(data_nascimento))