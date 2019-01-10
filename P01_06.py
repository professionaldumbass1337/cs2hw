def square(a):
    b = []
    for i in a:
        b.append(i**2)
    return b


print square([3,1,5,2,4]) # [9,1,25,4,16]
print square([7,6,3,1,5,8,2,4]) # [49,36,9,1,25,64,4,16]