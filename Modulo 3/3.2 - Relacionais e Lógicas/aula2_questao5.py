genero = input("Gênero: (M ou F)")
idade = int (input("Sua Idade: "))
tempo = int (input("Seu Tempo de Serviço (Em Anos): "))
print ((genero =='F' and idade >60 or genero == 'M' and idade > 65) or 
(tempo >29) or
(idade > 59 and tempo >24))