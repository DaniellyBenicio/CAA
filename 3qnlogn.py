def soma(nums, alvo):
    nums = [(num, i) for i, num in enumerate(nums)]
    nums.sort()
    esquerda = 0
    direita = len(nums) - 1
    while esquerda < direita:
        soma = nums[esquerda][0] + nums[direita][0]
        if soma == alvo:
            return [nums[esquerda][1], nums[direita][1]]
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1
    return []

nums = [2, 7, 11, 15]
X = 9
resultado = soma(nums, X)
print("nums: ", nums)
print("X: ", X)
print("Resultado:", resultado)
