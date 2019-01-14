def firstStr(s1, s2, s3):
    # ADD ADDITIONAL CODE HERE!
    return min(s1,s2,s3)

print firstStr("abcde","deabc","abc") # abc
print firstStr("bcde","ebcd","bedc") # bcde
print firstStr("abcde","bcd","abcd") # abcd
print firstStr("cde","abced", "bcd") # abced