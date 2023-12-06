'''Dado um array ordenado de inteiros distintos e um valor alvo, retorne o índice se o alvo for
encontrado. Caso contrário, retorne o índice onde estaria se fosse inserido na ordem.
Você deve escrever um algoritmo com complexidade de tempo de execução O(logn).
1 # Exemplo 1:
2 Entrada : nums = [1 ,3 ,5 ,6] , alvo = 5
3 Saida : 2
4 # Exemplo 2:
5 Entrada : nums = [1 ,3 ,5 ,6] , alvo = 2
6 Saida : 1'''

nums = [1, 3, 5, 6]
alvo = 5
esquerda = 0
direita = len(nums)

for i in range(len(nums)):
    meio = (esquerda + direita) // 2
    if nums[meio] == alvo:
        print(f"Alvo {alvo} encontrado no índice {meio}")
        break
    elif nums[meio] < alvo:
        esquerda = meio + 1
    else:
        direita = meio
else:
    print(f"Alvo {alvo} não encontrado no array. Seria inserido no índice {esquerda}")

