def multiplicar(A, B):
    C = []
    for i in range(len(A)):
        linha = []
        for i in range(len(A)):
            linha.append(0)
        C.append(linha)

    if len(A) == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        tamanho = len(A) // 3
        A11, A12, A13, A21, A22, A23, A31, A32, A33 = dividir(A, tamanho)
        B11, B12, B13, B21, B22, B23, B31, B32, B33 = dividir(B, tamanho)
        
        C11 = somar(multiplicar(A11, B11), multiplicar(A12, B21), multiplicar(A13, B31))
        C12 = somar(multiplicar(A11, B12), multiplicar(A12, B22), multiplicar(A13, B32))
        C13 = somar(multiplicar(A11, B13), multiplicar(A12, B23), multiplicar(A13, B33))
        C21 = somar(multiplicar(A21, B11), multiplicar(A22, B21), multiplicar(A23, B31))
        C22 = somar(multiplicar(A21, B12), multiplicar(A22, B22), multiplicar(A23, B32))
        C23 = somar(multiplicar(A21, B13), multiplicar(A22, B23), multiplicar(A23, B33))
        C31 = somar(multiplicar(A31, B11), multiplicar(A32, B21), multiplicar(A33, B31))
        C32 = somar(multiplicar(A31, B12), multiplicar(A32, B22), multiplicar(A33, B32))
        C33 = somar(multiplicar(A31, B13), multiplicar(A32, B23), multiplicar(A33, B33))
        
        C = unir_matrizes(C11, C12, C13, C21, C22, C23, C31, C32, C33, tamanho)

    return C

def extrair_submatriz(M, linha_inicio, linha_fim, coluna_inicio, coluna_fim):
    submatriz = []

    for i in range(linha_inicio, linha_fim):
        linha = []
        for j in range(coluna_inicio, coluna_fim):
            linha.append(M[i][j])
        submatriz.append(linha)
        
    return submatriz

def dividir(M, tamanho):
    M11 = extrair_submatriz(M, 0, tamanho, 0, tamanho)
    M12 = extrair_submatriz(M, 0, tamanho, tamanho, 2*tamanho)
    M13 = extrair_submatriz(M, 0, tamanho, 2*tamanho, 3*tamanho)
    M21 = extrair_submatriz(M, tamanho, 2*tamanho, 0, tamanho)
    M22 = extrair_submatriz(M, tamanho, 2*tamanho, tamanho, 2*tamanho)
    M23 = extrair_submatriz(M, tamanho, 2*tamanho, 2*tamanho, 3*tamanho)
    M31 = extrair_submatriz(M, 2*tamanho, 3*tamanho, 0, tamanho)
    M32 = extrair_submatriz(M, 2*tamanho, 3*tamanho, tamanho, 2*tamanho)
    M33 = extrair_submatriz(M, 2*tamanho, 3*tamanho, 2*tamanho, 3*tamanho)
    return M11, M12, M13, M21, M22, M23, M31, M32, M33


def unir_matrizes(M11, M12, M13, M21, M22, M23, M31, M32, M33, tamanho):
    M = []
    tam = 3 * tamanho
    for i in range(tam):
        linha = []
        for i in range(tam):
            linha.append(0)
        M.append(linha)

    for i in range(tamanho):
        for j in range(tamanho):
            M[i][j] = M11[i][j]
            M[i][j + tamanho] = M12[i][j]
            M[i][j + 2 * tamanho] = M13[i][j]
            M[i + tamanho][j] = M21[i][j]
            M[i + tamanho][j + tamanho] = M22[i][j]
            M[i + tamanho][j + 2 * tamanho] = M23[i][j]
            M[i + 2 * tamanho][j] = M31[i][j]
            M[i + 2 * tamanho][j + tamanho] = M32[i][j]
            M[i + 2 * tamanho][j + 2 * tamanho] = M33[i][j]
    return M


def somar(A, B, C):
    len(A)
    D = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A)):
            linha.append(A[i][j] + B[i][j] + C[i][j])
        D.append(linha)
    return D


def mostrar(matriz):
    for linha in matriz:
        print(linha)


A = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

matrizFinal = multiplicar(A, B)

print("Matriz A:")
mostrar(A)

print("\nMatriz B:")
mostrar(B)

print("\nMatriz C produto de A x B:")
mostrar(matrizFinal)


#Complexidade do tempo

'''
T(n) = 9T(n/3) + O(n²)

Usando o teorema Mestre
t(n) = aT(n/b) + f(n)
a = 9 subproblemas
b = 3
f(n) = n²
c = 2

como nlogba = nlog39 = n2,então n² = f(n) adentra ao 2 caso do teorema mestre. 
Se f(n)=Θ(nlogba), então T(n)=Θ(nlogbalgn) --> n²logn
'''