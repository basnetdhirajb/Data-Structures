def fibonacciByIter(n):
    first = 0
    second = 1
    
    if n == 0:
        return first
    
    if n == 1:
        return second
    
    next = 0
    for i in range(2,n+1):
        next = first + second
        first = second
        second = next
    
    return next

def fibonacciByRec(n):
    
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    return fibonacciByRec(n-1) + fibonacciByRec(n-2)

#0,1,1,2,3,5,8,13
    
print(fibonacciByIter(40))
print(fibonacciByRec(40))