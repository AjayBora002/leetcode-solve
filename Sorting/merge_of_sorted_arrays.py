def merge(left, right):
    result=[]
    i, j=0,0
    n=len(left)
    m=len(right)
    while i<n and j<m:
        if left[i]< right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1

    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result






