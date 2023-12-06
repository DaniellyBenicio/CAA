'''Dado um array inteiro nums classificado em ordem não decrescente, retorne um array dos qua-
drados de cada número classificado em ordem não decrescente.

Example 1:
Entrada: nums = [−4, −1, 0, 3, 10]
Saida: [0,1,9,16,100]'''

nums = [-4, -1, 0, 3, 10]

quadrado = []

for i in nums: #O(n)
    quadrado.append(i**2)

print("Ordem não decrescente: ", nums)
print("Nums ao quadrado: ", quadrado)
quadrado.sort()#O(nlogn)
print("Ordem crescente: ", quadrado)


#logo quem domina é #O(nlogn)