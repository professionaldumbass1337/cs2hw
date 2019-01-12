def delete(L, e):
    # ADD ADDITIONAL CODE HERE!
    M = []
    for i in range(len(L)):
        if L[i] != e:
            M.append(L[i])
    return M

print delete([2,5,7,3,2,8,3,3],3) # [2,5,7,2,8]
print delete([2,3,7,3,2,8,3,3],2) # [3,7,3,8,3,3]
print delete([2,2,7,2,2,2,2,2],2) # [7]