nums = [-4, -1, 0, 3, 10]
resultado = [0] * len(nums)
esquerda = 0
direita = len(nums) - 1

for i in range(len(nums) - 1, -1, -1):
    quadrado_esquerda = nums[esquerda] ** 2
    quadrado_direita = nums[direita] ** 2


    if quadrado_esquerda > quadrado_direita:
        resultado[i] = quadrado_esquerda
        esquerda += 1
    else:
        resultado[i] = quadrado_direita
        direita -= 1

print("Array inicial: ", nums)
print("Array ordenado ao quadrado: ", resultado)

