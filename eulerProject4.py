#Project Euler Problem 4: Largest palindrome made from the product of two 3 digit numbers

def isPalindrome(n):
    
    firstHalf = []
    nString = str(n) #convert integer to string
    nList = list(nString)
    if len(nString) % 2 == 0: #checks to see if the number of characters in the string is an even number
        #even                       
        for i in range(len(nString)//2):
            firstHalf.append(nString[i]) #makes an array that's the first half of the number
            del nList[0] #deletes the first half of the array, thus making it an array of the second half of the number

        nList.reverse()#reverses the second half array, so we can compare and see if it equals the first half
        if nList == firstHalf:
            
            return True
        else:
    
            return False
            
    else:
        #odd
       
        del nList[len(nString)//2] #deletes the middle digit, since it doesn't matter what it is for a palindrome

        for i in range(len(nString)//2):
            firstHalf.append(nString[i])
            del nList[0]

        nList.reverse()

        if nList == firstHalf:
            
            return True
        else:
            
            return False
        

palindromes = []

a=99
b=99
for i in range(900):
    a = a + 1
    b = 99
    for j in range(900):
        b= b + 1
        #print("a is ", a, "b is ", b)
        product = a * b
        if(isPalindrome(product)):
            palindromes.append(product)

palindromes.sort()
print(palindromes)



oddNumber = 631564163
oddNumberPalindrome = 12345654321

print(isPalindrome(oddNumber))
print(isPalindrome(oddNumberPalindrome))
print(isPalindrome(1555225551))

