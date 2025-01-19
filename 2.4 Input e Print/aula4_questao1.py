comprimento = float(input("Insira o valor do comprimento: "))
largura = float (input("Insira o valor da Largura: "))
preco_m2 = float (input("Insira o preço do m² na região: "))

area_m2 = largura * comprimento
preco_total = preco_m2 * area_m2

print(f"O terreno Possui {area_m2}m² e custa R${preco_total:,}")
