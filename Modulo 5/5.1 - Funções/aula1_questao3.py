import random
n = random.randint(1, 10)

while True:
    adv = int(input("Adivinhe o número entre 1 e 10: "))
    if adv < n:
        print("Miuto baixo, tente novamente!")
    elif adv > n:
        print("Miuto alto, tente novamente!")
    else: 
        print("Correto! o númre é: ", n)
        break