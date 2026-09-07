def b2d(b:str) -> int:
    deci = 0
    power = 0
    index = len(b)-1
    while index>=0:
        num = int(b[index])*(2**power)
        deci+=num
        index-=1
        power+=1
    return deci
b = "100"
a=b2d(b)
print(a)







