def selection_sort_crestente(lista):
    for i in range(len(lista)):
        # Assume que o menor é o atual
        menor = i

        # Procura o menor no resto da lista
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        # Troca o menor com o número na posição i
        lista[i], lista[menor] = lista[menor], lista[i]

    return lista

print(selection_sort_crestente([7, 3, 5, 2, 8, 1, 4, 6, 9, 0, 10]))


def selection_sort_decrescente(lista):
    for i in range(len(lista)):
        # Assume que o maior é o atual
        maior = i

        # Procura o maior no resto da lista
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[maior]:
                maior = j

        # Troca o maior com o número na posição i
        lista[i], lista[maior] = lista[maior], lista[i]

    return lista

print(selection_sort_decrescente([7, 3, 5, 2, 8, 1, 4, 6, 9, 0, 10]))
