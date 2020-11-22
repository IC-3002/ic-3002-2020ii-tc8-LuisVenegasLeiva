def verificar_ruta(x, y,M,N):
    return not (x < 0 or y < 0 or x >= M or y >= N)
 
 
def contar_rutas_mas_cortas(C):
    N = len(C)
    M = len(C[1])

    count = 0
 
    revisadas = [[False for x in range(N)] for y in range(M)]
 

    count = buscar(C, 0, 0, revisadas, count,M,N)
    return count


def buscar(C, x, y, revisadas, count, M, N):
    if x == M - 1 and y == N - 1 and C[N-1][M-1]==1:
        return count
    if x == M - 1 and y == N - 1:
        return count + 1
 

    revisadas[x][y] = True
 

    if verificar_ruta(x, y, M, N) and C[x][y] == 0:
 
        if x + 1 < M and not revisadas[x + 1][y]:
            count = buscar(C, x + 1, y, revisadas, count, M, N)
 
        if y + 1 < N and not revisadas[x][y + 1]:
            count = buscar(C, x, y + 1, revisadas, count, M, N)

    revisadas[x][y] = False
    return count
'''
C =[[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

contar_rutas_mas_cortas(C)
'''