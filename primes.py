"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError()
    list = [2]
    firstNum = 3
    while len(list)!= number_of_primes:
        if checkIfPrime(firstNum):
            list.append(firstNum)
        firstNum = firstNum + 1
    return list

def checkIfPrime(num):
    for i in range(2, num//2+1):
        if (num%i == 0):
            return False
    return True