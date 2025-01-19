valor = int(input("Digite o valor em reais: "))

nota_100 = valor // 100
valor = valor % 100

nota_50 = valor // 50
valor = valor % 50

nota_20 = valor // 20
valor = valor % 20

nota_10 = valor // 10
valor = valor % 10

nota_5 = valor // 5
valor = valor % 5

nota_2 = valor // 2
valor = valor % 2

nota_1 = valor // 1

print(f"{nota_100} nota(s) de R$100,00")
print(f"{nota_50} nota(s) de R$50,00")
print(f"{nota_20} nota(s) de R$20,00")
print(f"{nota_10} nota(s) de R$10,00")
print(f"{nota_5} nota(s) de R$5,00")
print(f"{nota_2} nota(s) de R$2,00")
print(f"{nota_1} nota(s) de R$1,00")