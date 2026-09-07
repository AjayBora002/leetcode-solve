matrix = [[1,0,1],[1,2,0],[2,9,1]]
r = len(matrix)
l=len(matrix[0])
row_track = [0 for _ in range(r)]
col_track = [0 for _ in range(l)]
for i in range(0, r):
    for j in range(0, l):
        if matrix[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1
for i in range(0, r):
    for j in range(0, l):
        if row_track[i] == -1 or col_track[j] == -1:
            matrix[i][j] = 0







matrix = [[1,0,1],[1,2,0],[2,9,1]]
