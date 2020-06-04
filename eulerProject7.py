#Project Euler Problem 7: What is the 10,001 prime number?

def isPrime(r):
    for i in range(r):
        if i > 1:
            if r%i == 0:
                return False

    return True

primes = []
n = 2
while len(primes) < 10001:
    #print(primes)
    if isPrime(n):
        primes.append(n)
    n += 1

print(primes[10000])

