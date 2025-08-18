def soma_matrizes(X, Y):
    """Retorna a soma elemento a elemento das matrizes X e Y."""
    n = len(X)              # número de linhas
    m = len(X[0])           # número de colunas (assumindo X e Y têm mesma dimensão)
    resultado = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            resultado[i][j] = X[i][j] + Y[i][j]
    return resultado

def multiplicacao_matrizes_recursiva(X, Y):
    """Multiplica duas matrizes quadradas X e Y usando divisão e conquista recursiva."""
    n = len(X)
    # Caso base: matriz 1x1, retorna multiplicação direta
    if n == 1:
        return [[ X[0][0] * Y[0][0] ]]
    # Particiona X e Y em 4 submatrizes cada
    m = n // 2
    A = [ [elem for elem in row[:m]]   for row in X[:m] ]   # quadrante A (sup. esq de X)
    B = [ [elem for elem in row[m:]]   for row in X[:m] ]   # quadrante B (sup. dir de X)
    C = [ [elem for elem in row[:m]]   for row in X[m:] ]   # quadrante C (inf. esq de X)
    D = [ [elem for elem in row[m:]]   for row in X[m:] ]   # quadrante D (inf. dir de X)
    E = [ [elem for elem in row[:m]]   for row in Y[:m] ]   # quadrante E (sup. esq de Y)
    F = [ [elem for elem in row[m:]]   for row in Y[:m] ]   # quadrante F (sup. dir de Y)
    G = [ [elem for elem in row[:m]]   for row in Y[m:] ]   # quadrante G (inf. esq de Y)
    H = [ [elem for elem in row[m:]]   for row in Y[m:] ]   # quadrante H (inf. dir de Y)
    # Calcula recursivamente os produtos dos sub-blocos e soma os resultados
    Z11 = soma_matrizes( multiplicacao_matrizes_recursiva(A, E),
                         multiplicacao_matrizes_recursiva(B, G) )
    Z12 = soma_matrizes( multiplicacao_matrizes_recursiva(A, F),
                         multiplicacao_matrizes_recursiva(B, H) )
    Z21 = soma_matrizes( multiplicacao_matrizes_recursiva(C, E),
                         multiplicacao_matrizes_recursiva(D, G) )
    Z22 = soma_matrizes( multiplicacao_matrizes_recursiva(C, F),
                         multiplicacao_matrizes_recursiva(D, H) )
    # Combina os quatro quadrantes na matriz resultado Z
    Z = [ Z11[i] + Z12[i] for i in range(m) ] + \
        [ Z21[i] + Z22[i] for i in range(m) ]
    return Z
