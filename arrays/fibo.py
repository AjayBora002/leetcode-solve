def fibo(n):
    if n<=1:
        return n
    a, b=0, 1
    for i in range (2, n+1):
        a, b = b, a+b
    return b
print(fibo(5))



def fib_iterative(n):
    if n <= 1:
        return n
    
    # We only need the last two numbers to calculate the next one
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        # Update a and b to move the window forward
        a, b = b, a + b
        
    return b

print(fib_iterative(7))





