def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho_min = min(len(lista1), len(lista2))

    for i in range(tamanho_min):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    lista_intercalada.extend(lista1[tamanho_min:])
    lista_intercalada.extend(lista2[tamanho_min:])

    return lista_intercalada

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i + 1}º elemento da lista 1: ")) for i in range(n1)]

n2 = int(input("\nDigite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i + 1}º elemento da lista 2: ")) for i in range(n2)]

lista_intercalada = intercalar_listas(lista1, lista2)

print("\nLista intercalada:", lista_intercalada)