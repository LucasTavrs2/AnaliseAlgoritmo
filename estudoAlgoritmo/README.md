## https://github.com/egonschiele/grokking_algorithms

# Selection Sort
 - O(n^2)
 - In-place
 - Não é estável
 - Divide a lista em duas partes, a parte ordenada e a parte não ordenada.
 - A cada iteração, o menor elemento da parte não ordenada é adicionado ao final da parte ordenada.
 - A complexidade de tempo é O(n^2) no pior caso e O(n^2) no melhor caso.
 - A complexidade de espaço é O(1) pois é um algoritmo in-place.
 - Não é um algoritmo estável pois a ordem dos elementos iguais pode ser alterada.

#Merge Sort
 - O(n log n)
 - Não é in-place
 - É estável
 - Divide a lista em duas partes, ordena cada parte e depois junta as duas partes ordenadas.
 - A complexidade de tempo é O(n log n) no pior caso e O(n log n) no melhor caso.
 - A complexidade de espaço é O(n) pois é necessário espaço adicional para armazenar as listas temporárias.
 - É um algoritmo estável pois a ordem dos elementos iguais é mantida.