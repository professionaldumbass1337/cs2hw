def countA(s):
    # ADD ADDITIONAL CODE HERE!
    count = 0
    for i in s:
        if i == 'A':
            count += 1

    return count

print countA("AbAA") # 3
print countA("bcdAAAdfAA") # 5
print countA("abc") # 0