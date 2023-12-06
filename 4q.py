nums = [2, 7, 1, 3, 2, 2]

majoritario = nums[0]
contagem = 0

for i in range(len(nums)): 
    if contagem == 0:
        majoritario = nums[i]
        contagem = 1
    elif nums[i] == majoritario:
        contagem += 1
    else:
        contagem -= 1

print("Array: ", nums)
print("Elemento majoritário do array:", majoritario)

