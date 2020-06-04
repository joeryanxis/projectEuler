#Project Euler Problem 3: Largest prime factor of 600851475143

def isPrime(r):
    for i in range(r):
        if i > 1:
            if r%i == 0:
                return False

    return True


q = 600851475143

#q = 1003195 #for testing purposes


primeArray = []
primeFactors = []
prime = True

for i in range(q//2): 
    if i > 1:
        if q % i == 0:
            if isPrime(i):
                print(i)
                primeFactors.append(i)

print(primeFactors)
            
            
            



