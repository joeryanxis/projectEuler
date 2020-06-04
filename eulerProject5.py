#Project Euler Problem 5: Smallest number evenly divisibly by all numbers from 1 to 20

def isDivisible(n): #function for seeing if n is evenly divisible by numbers in a range
    
    for i in range(20): #range from 0 through 19
        i = i + 1       #need i to equal 1 through 20 though
        if n % i == 0:  #checks to see if n is evenly divisibly by what i currently is
            divisible = True
        else:
            divisible = False
            
            break       #one false is enough, break the loop

    if divisible == True:
        return True
    else:
        return False

n = 2520                #math trick: the problem gives us 2520 as the smallest number evenly divisible
                        #by the numbers 1-10, and so we can step by multiples of this number and save a
                        #lot of time not checking the numbers in between, which we know would not be
                        #evenly divisible
while n > 0:
    if isDivisible(n):
        print(n)
        break
    else:
        n += 2520
        continue
    
        
