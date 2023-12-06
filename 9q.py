'''(Algoritmos recursivos) Determine a função de complexidade, das funções recursivas apresentadas
abaixo, fazendo as considerações que considerar pertinente.

# Primeira
def Pesquisa1 (A , n ) :            O(1)
    if n > 1:                       O(1)
        InspecioneNElementos = n * n * n        # custo n^3
        Pesquisa1 (A , n // 3)      O(log3n)


R =  Na condição if, realiza InspecioneNElementos = n * n * n, caso seja verdadeira. Logo o custo
é O(n³) pois é n * n * n. Em seguida, a função chama a si mesma com n // 3 como o novo valor de n, ou seja,
o problema é didivido em um terço do seu tamanho a cada chamada. Portanto, o número total de chamadas recursivas 
será aproximadamente log base 3 de n (log₃ n). Então o produto final é O(n³) * log3n = O(n³log3n). 
O tempo de execução vai sempre aumentar de forma proporcional ao cubo do tamanho da entrada 
multiplicado pelo logaritmo base 3 do tamanho da entrada.


# Segunda
def Pesquisa2 (A , n):              O(1)
    if n <= 1:                      O(1)
        return                      O(1)
    else :                          O(1)
    # obtenha o maior elemento entre os elementos O(n)
    # de alguma forma isso permite descartar 2/5 dos elementos e fazer uma chamada recursiva no resto
        Pesquisa2 (A , 3 * n // 5)


R = Chama a si mesmo com 3 * n // 5. Então o número total de chamadas é O(nlog(5/3)n).
O que implica que o tempo  de execução aumenta de forma proporcional ao logaritmo base 5/3 do tamanho da entrada.


# Terceira
def Pesquisa3 (A , n):               O(1)
    if n <= 1:                       O(1)
        return                       O(1)
    else:                            O(1)
    # ordena os elementos   
    # de alguma forma isso permite descartar 1/3 dos elementos e fazer uma chamada recursiva no resto
        Pesquisa3 (A , 2 * n // 3)


R = Usando o teorema mestre --> T(n) = aT(n/b) + f(n)
a = 1
b = 3/2
f(n) = O(1), pois a parte não recursiva da função tem tempo constante.
Desse modo, função tem complexidade de tempo O(nlog n), devido o problema ser dividido por uma constante (3/2), 
resultando em um algoritmo de tempo logarítmico.


# Magica !!
class Item :
    def __init__ ( self , Chave ) :
        self. Chave = Chave

def Enigma2 (A , m , n , i , j ) :
    x = A [( i + j ) // 2]                                      --> O(1) 
    while True:                                                 --> O(n)
        while x . Chave > A [ i ]. Chave :                      --> O(n)
            i += 1                                              --> O(1) 
        while x . Chave < A [ j ]. Chave :                      --> O(n)
            j -= 1                                              --> O(1) 
        if i <= j :                                             --> O(1) 
            A [ i ] , A [ j] = A [ j ] , A [ i ]                --> O(1) 
            i += 1                                              --> O(1) 
            j -= 1                                              --> O(1) 
        if i > j :                                              --> O(1) 
            break
        
            
def Enigma1 (A , m , n ) :                                     --> O(1) 
    i , j = 0 , 0                                              --> O(1) 
    Enigma2 (A , m , n , i , j )                               --> O(n) 
    if m < j :                                                 --> O(1) 
        Enigma1 (A , m , j )                                   --> O(n log n) no caso médio, O(n²) no pior caso 
    if i < n :                                                 --> O(1) 
        Enigma1 (A , i , n )                                   --> O(n log n) no caso médio, O(n²) no pior caso 
        
        
            
R = O algoritmo implementado espelha-se no QuickSort. O enigma2 particiona o vetor em torno do pivo X. X é escolhido
sendo o elemento referente ao meio do array. A complexidade aqui é O(n). A função enigma1 é a parte recursiva que
fica chamando recursivamente a função enigma2 para ir particionando o vetor e depois a si mesma para os subvetores a 
E e D do pivô x. A complexidade desse caso de dividir para conquistar é O(n log n) no melhor e médio caso e 
no pior caso O(n²).'''