#O((m + n)log(m + n))

nums1 = [1,2,3, 0, 0, 0]
m = 3
nums2 = [2,5,6]
n = 3

def mesclar(nums1, m, nums2, n):
    novonums = nums1[:m] + nums2

    novonums.sort()

    for i in range(m+n):
        nums1[i] = novonums[i]

print("Array 1: ", nums1)
print("Array 2: ",nums2)

mesclar(nums1, m, nums2, n)

print("Array mesclado: ", nums1)