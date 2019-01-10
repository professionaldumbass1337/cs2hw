def countZero(numbers):
    count = 0
    for i in numbers:
        if i == 0:
            count += 1

    return count


print countZero([0,4,0,-2,4,0]) # 3
print countZero([1,0,-2,4,0,0,-7,0,5]) # 4