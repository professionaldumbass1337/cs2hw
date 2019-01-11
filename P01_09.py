# "for all" pattern
def isPrime(p):
    b = int(p**0.5)
    for i in range(2,b+1):
        if p%i == 0:
            return False
    return True


# "for some" pattern
def somePrime(numbers):
    # ADD ADDITIONAL CODE HERE!
    for i in range(len(numbers)):
        if isPrime(numbers[i]):
            return True
    return False


# "for all" pattern
def allPrime(numbers):
    # ADD ADDITIONAL CODE HERE!
    for i in range(len(numbers)):
        if not isPrime(numbers[i]):
            return False
    return True


num1 = [217, 287, 143, 163, 319]
num2 = [217, 287, 143, 169, 319]
num3 = [223, 281, 227, 151, 149]
print somePrime(num1), allPrime(num1) # True False
print somePrime(num2), allPrime(num2) # False False
print somePrime(num3), allPrime(num3) # True True