produto_1 = input("Digite o nome do produto 1: ")
preco_produto_1 = float(input ("Digite o preço unitário do produto 1: "))
quantidade_produto_1 = int(input("Digite a quantidade do produto  1: "))

produto_2 = input("Digite o nome do produto 2: ")
preco_produto_2 = float(input("Digite o preço unitário do produto 2: "))
quantidade_produto_2 = int(input("Digite a quantidade do produto 2: "))

produto_3 = input("Digite o nome do produto 3: ")
preco_produto_3 = float(input("Digite o preço unitário do produto 3: "))
quantidade_produto_3 = int(input("Digite a quantidade do produto 3: "))

total = preco_produto_1 * quantidade_produto_1 + preco_produto_2 * quantidade_produto_2 + preco_produto_3 * quantidade_produto_3

print(f"Total: R${total:,.2f}")