N = int(input("Digite a quantidade de respondentes: "))

if N <= 0:
    print("A quantidade de respondentes deve ser maior que zero.")
else:
    soma_idades = 0 

    for i in range(N):
        idade = int(input(f"Digite a idade do respondente {i + 1}: "))
        soma_idades += idade 

    media = soma_idades / N

    print(f"A média de idade dos respondentes é: {media:.2f}")