#O(n²)

def soma(nums, alvo):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == alvo:
                return [i, j]
    return []

nums = [2, 7, 11, 15]
X = 9
resultado = soma(nums, X)

print("Entrada:", "nums =", nums)
print("X =", X)
print(resultado)

