def same(L1, L2):
    # ADD ADDITIONAL CODE HERE!
    return True if sorted(L1) == sorted(L2) else False

print same([2,3,2,7],[2,7,2,3]) # True
print same([2,5,7,8],[2,3,4,5]) # False
print same([1,1,2,3],[1,2,1,3]) # True
print same([2,3,5,5],[2,2,5,3]) # False