class Solution:

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if self.is_safe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                self.solve(col + 1, board, ans, n)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def is_safe(self, row, col, board, n):
        duprow = row
        dupcol = col

        # Upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Straight left (same row)
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        # Lower-left diagonal
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        return True

    def solveQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

if __name__ == "__main__":
    n = 4
    obj = Solution()
    solutions = obj.solveQueens(n)

    print(f"Total solutions for N = {n}: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()



        # Time Complexity: O(N!.N)
        # S.C: O(N^2)
















class Solution:
    def solve(self, col, board, ans, leftrow, lowerdiagonal, upperdiagonal, n):
        if col==n:
            ans.append(board[:])
            return

        for row in range(n):
            if (
                leftrow[row] == 0 and
                lowerdiagonal[row+col] == 0 and
                upperdiagonal[n-1 + col-row] ==0
            ):
                board[row] =  board[row][:col] + "Q" + board[row][col+1 :]
                leftrow[row] = 1
                lowerdiagonal[row+col]  =1
                upperdiagonal[n-1+col-row] = 1
                self.solve(col+1, board, ans, leftrow, lowerdiagonal, upperdiagonal, n)
                board[row] = board[row][:col] + "." + board[row][col+1: ]
                leftrow[row]= 0
                lowerdiagonal[row+col] = 0
                upperdiagonal[n-1+col-row] = 0


    def solveQueens(self, n):
        ans= []
        board = ["."*n for _ in range(n)]
        leftrow= [0]*n
        lowerdiagonal = [0] * (2*n-1)
        upperdiagonal = [0] * (2*n-1)
        self.solve(0, board, ans, leftrow, lowerdiagonal, upperdiagonal, n)
        return ans                