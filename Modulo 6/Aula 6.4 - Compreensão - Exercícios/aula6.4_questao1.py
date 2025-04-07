pares = [z for z in range (20, 51) if z%2==0]
print(pares)

quadrados = [p**2 for p in range (1, 10)]
print (quadrados)

num = [n for n in range (1, 100) if n%7==0]
print(num)

parimpar_num = [num for num in range (0, 30, 3)]
print(parimpar_num)

parimpar = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print (parimpar)