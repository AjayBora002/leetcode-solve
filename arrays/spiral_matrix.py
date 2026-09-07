def spiral(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    top, left = 0, 0
    bottom, right = len(matrix)-1, len(matrix[0])-1
    while top<=bottom and left<=right:
        for i in range (left, right+1):
            result.append(matrix[top][i])
        top+=1
        for i in range (top, bottom+1):
            result.append(matrix[i][right])
        right-=1
        if top<=bottom: # yha pr if again isliye use kiya kyuki if test case has only 1 row then after goinf from lrft to right it will come agin to left 
            for i in range (right, left-1, -1):# we used -1 because we are going in backward directtion
                result.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range (bottom, top-1, -1):
                result.append(matrix[i][left])
            left+=1
    return result
        















