#Project Euler Problem 2: Find the sum of even fibonacci numbers under 4 million

limit = 4000000

fibArray = [1,2]

for i in range(limit):
    nextNumber = fibArray[i] + fibArray[i+1]
    
    fibArray.append(nextNumber)
    
    if nextNumber >= limit:
        break
x = 0
for i in fibArray:
    print(i)
    if i%2 == 0:
        x = x + i

print(x)

