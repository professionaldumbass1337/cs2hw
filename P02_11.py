def replace(s, c, to):
    # ADD ADDITIONAL CODE HERE!
    r = ""
    for i in s:
        if i == c:
            r += to
        else:
            r += i

    return r

print replace("abc","a","b") # bbc
print replace("abcDFabc","c","DD") # abDDDFabDD
print replace("abcdddd","d","fg") # abcfgfgfgfg