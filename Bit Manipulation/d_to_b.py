def d2b(x):
    if x == 0:
        return "0"
    
    r = ""
    while x > 0:
        r += str(x % 2)  
        x = x // 2
    
    return r[::-1]