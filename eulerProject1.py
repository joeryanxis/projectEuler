#Project Euler Problem 1: Sum of multiples of 3 and 5 under 1000

multiplesOfThree = []
multiplesOfFive = []

multiplesNoDuplicates = []

x = 3
for i in range(1000):
    multiplesOfThree.append(x)
    x = x + 3
    if x >= 1000:
        break

print(multiplesOfThree)

y = 5
for i in range(1000):
    multiplesOfFive.append(y)
    y = y + 5
    if y >= 1000:
        break
    
print(multiplesOfFive)

for i in multiplesOfThree:
    if i not in multiplesOfFive:
        print("removed ", i)
        multiplesOfFive.append(i)
        
print(multiplesOfFive)
x = 0
for i in multiplesOfFive:
    x = x + i
print(x)
