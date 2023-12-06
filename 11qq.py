#O(m + n)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def mesclar(nums1, m, nums2, n):
    for i in range(m+n-1, -1, -1): 
        if m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
        elif n > 0:
            nums1[:n] = nums2[:n]
            break

print("Array 1: ", nums1)
print("Array 2: ",nums2)

mesclar(nums1, m, nums2, n)

print("Array mesclado: ", nums1)