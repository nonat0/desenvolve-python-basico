classe = input("Escolha sua classe (arqueiro, guerreiro ou mago): ")
forca = int(input("digite os pontos de força (de 1 a 20): "))
magia = int(input("digite os pontos de magia (de 1 a 20): "))
print((classe == 'mago' and forca < 11 and magia > 14) or (classe == 'guerreiro' and forca > 14 and magia < 11) or (classe == 'arqueiro' and forca > 5 and forca < 16 and magia > 5 and magia < 16))