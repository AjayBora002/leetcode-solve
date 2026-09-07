matrix = [[1,0,1],[1,2,0],[2,9,1]]
r = len(matrix)
for i in range(0, r-1):
    for j in range (i+1,r):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range (0, r):
    matrix[i].reverse()







