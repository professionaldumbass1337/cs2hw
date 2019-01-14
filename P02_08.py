def countChar(s, c):
    # ADD ADDITIONAL CODE HERE!
    count = 0
    for i in s:
        if i == c:
            count += 1

    return count

print countChar("AbAA","b") # 1
print countChar("AbAA","A") # 3
print countChar("DbDD","D") # 3
print countChar("bcdAAAdfAA","A") # 5
print countChar("abc","A") # 0