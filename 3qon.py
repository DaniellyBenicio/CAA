#O(n)

def soma(nums, alvo):
    dic = {}

    for i, num in enumerate(nums):
        complemento = alvo - num
        if complemento in dic:
            return [dic[complemento], i]
        dic[num] = i

    return []

nums = [2, 7, 11, 15]
X = 9
resultado = soma(nums, X)
print("nums: ", nums)
print("X: ", X)
print("Resultado:", resultado)
