#Finding factorial using both recursive and iterative ways

def findFactorialRec(num):
    factorial = 1
    
    for i in range(1, num+1):
        factorial*=i
    
    return factorial
    
    
def findFactorialFac(num):
    #Find base case
    #Find iterative case
    #2 returns maybe
    
    if num == 1:
        return 1
    else:
        return findFactorialFac(num-1)
     

print(findFactorialRec(30))