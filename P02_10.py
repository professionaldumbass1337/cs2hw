def delete(s, c):
    # ADD ADDITIONAL CODE HERE!
    r = ""
    for i in range(len(s)):
        if s[i] != c:
            r += s[i]
    return r

print delete("abc","a") # bc
print delete("abcDFabc","c") # abDFab
print delete("abcdddd","d") # abc