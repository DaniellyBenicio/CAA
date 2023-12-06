'''Uma subsequência é palíndroma se ela é igual lendo da direita para esquerda ou lendo da esquerda para direita. 
Por exemplo, a sequência (ACGT GT CAAAAT CG) possui muitas subsequências
palíndromas, como (ACGCA) e (AGT GA). Mas a subsequência (ACT) não é palíndroma. Escreva um algoritmo O(n²) 
que recebe uma sequência S[1 . . . n] e retorna a subsequência palíndroma de tamanho máximo.'''

seq = "ACGTGTCAAAATCG"
tam = 0
inicio = 0

for i in range(len(seq)):
    for j in range(i, len(seq)):
        if seq[i:j+1] == seq[j:i-1:-1] and (j - i + 1) > tam:
            inicio = i
            tam = j - i + 1

print("A sequência recebida: ", seq)
print("Maior subsequência palindrômica: ", seq[inicio:inicio+tam])
