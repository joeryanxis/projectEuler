#Project Euler Problem 6: Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum

sumOfSquares = 0
squareOfSum = 0
n = 0
for i in range(100):
    i += 1
    sumOfSquares = sumOfSquares + (i * i)

for i in range(100):
    i += 1
    n = n + i

squareOfSum = n * n

print(squareOfSum - sumOfSquares)
    

#print(sumOfSquares)
    
