def verificar_ruta(x, y,M,N):
    return not (x < 0 or y < 0 or x >= M or y >= N)
 
def contar_rutas_mas_cortas(C):
    N = len(C)
    M = len(C[1])

    contador = 0
 
    revisadas = [[False for x in range(N)] for y in range(M)]
 
    contador = buscar(C, 0, 0, revisadas, contador,M,N)
    return contador

def buscar(C, x, y, revisadas, contador, M, N):
    if x == M - 1 and y == N - 1 and C[N-1][M-1]==1:
        return contador
    if x == M - 1 and y == N - 1:
        return contador + 1

    revisadas[x][y] = True

    if verificar_ruta(x, y, M, N) and C[x][y] == 0:
        if x + 1 < M and not revisadas[x + 1][y]:
            contador = buscar(C, x + 1, y, revisadas, contador, M, N)
 
        if y + 1 < N and not revisadas[x][y + 1]:
            contador = buscar(C, x, y + 1, revisadas, contador, M, N)

    revisadas[x][y] = False
    return contador
'''
C =[[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

contar_rutas_mas_cortas(C)
'''