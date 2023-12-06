'''
def bubble_sort (A , n ) :      --> Tempo constante O(1)
    for j in range ( n ) :        --> O(n)
        for i in range ( n - 1) :        --> O(n)
            if A [ i ] > A [ i + 1]:        --> O(1)
                aux = A [ i ]        --> O(1)
                A [ i ] = A [ i + 1]        --> O(1)
                A [ i + 1] = aux        --> O(1)

No melhor caso O(n) quando a entrada já está ordenada, então realizaria troca, seria o mínimo de trabalho.
No pior caso: O(n²) onde o algoritmo está totalmente desordenado e cada elemento deve ser comparado e trocado, de um por um.
No médio caso: O(n²) onde o algoritmo precisa fazer uma quantidade quadrática de comparações e trocas, 
considera-se todas as possíveis instâncias e mede-se o tempo médio. o desempenho dependerá da distribuição dos dados
 no array, então também será O(n²).

'''


'''
def bubble_sort2 (A , n ) :                --> Tempo constante O(1)
    troca = True                           --> O(1)
    while troca :                          --> O(n)
        troca = False                      --> O(1)
        for i in range ( n - 1) :          --> O(n)
            if A [ i ] > A [ i + 1]:       --> O(1)
            aux = A [ i ]                  --> O(1)
            A [ i ] = A [ i + 1]           --> O(1)
            A [ i + 1] = aux               --> O(1)
            troca = True

            
A complexidade do algoritmo assim como no exemplo acima é O(n²) no pior e médio caso.
No melhor caso, quando o array já está ordenado, não é preciso fazer trocas, 
logo, só precisa percorrer o algoritmo uma vez para verificar
o ordenamento, neses caso o melhor tempo O(n).
'''

'''Comparando os dois algoritmos de bubble sort, o segundo caso é mais eficiente para o melhor caso, 
tendo em vista a verificação de troca. Essa verificação melhora a eficiência no melhor caso para O(n).'''

def AlgumaCoisa(n):
    x = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            for k in range(1, j + 1):
                x = x + 1
    return x

print(AlgumaCoisa(3))

'''
def AlgumaCoisa ( n ) :               --> O(1)
    x = 0                             --> O(1)
    for i in range (1 , n ):          --> O(n)
        for j in range ( i + 1 , n + 1): --> O(n)
            for k in range (1 , j + 1):  --> O(n)
                x = x + 1            --> O(1)         
                       
              
A complexidade de tempo é avaliada pela quantidade de trabalho que o código precisa fazer em relação
ao tamanho da entrada, n. Então, independente da entrada de N é utilizado os 3 loops. 
Nesse caso, a complexidade desse algoritmo é O(n) * O(n) * O(n) nos 3 casos. 
Pois não tem variação na quantidade de trabalho que é realizada independente da entrada.'''


'''
def AlgumaCoisa2 ( n ) :                --> O(1)
    x = 0                               --> O(1)
    for i in range (1, n + 1) :        --> O(n)
        for j in range ( i + 1, n ):   --> O(n)
            for k in range (1, j + 1): --> O(n)
                x = x + 1               --> O(1)
A complexidade desse algoritmo também é O(n) * O(n) * O(n), logo O(n³) no pior caso, médio e melhor caso. Porque
 o número de operações aumenta sempre de forma proporcional (cúbica) do tamanho da n.
 
'''
'''Embora os dois algoritmos possuam a mesma complexidade, eles se diferem pelos os loops. No primeiro algoritmo, 
o 2 laço vai de i + 1 até n + 1. No segundo algoritmo, o segundo loop vai de i + 1 até n. 
Essa variação leva a uma contagem extra para cada valor de i no primeiro algoritmo, ou seja, quando aplicado/executado,
há um valor maior para x em comparação com o segudno algoritmo. Dessa forma, são complexidades iguais, mas com 
comportamentos e resultados distintos para a mesma entrada. Isso resulta em uma contagem extra para cada valor de i
 no primeiro algoritmo, levando a um valor final maior para x em comparação com o segundo algoritmo.'''

def AlgumaCoisa2(n):
    x = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            for k in range(1, j + 1):
                x = x + 1
    return x

print(AlgumaCoisa2(3))

