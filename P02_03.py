def kthSmallest(L, k):
    # ADD ADDITIONAL CODE HERE!
    L.sort()
    return L[k-1]

print kthSmallest([3,4,2,8,8], 1) # 2
print kthSmallest([3,4,2,8,8], 2) # 3
print kthSmallest([3,4,2,8,8], 3) # 4
print kthSmallest([3,4,2,8,8], 4) # 8
print kthSmallest([3,4,2,8,8], 4) # 8