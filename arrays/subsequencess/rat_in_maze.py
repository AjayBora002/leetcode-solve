# Given a square binary matrix maze[][] containing values 0 and 1, find all possible paths for a rat to travel from the top-left cell to the bottom-right cell. The rat can move in four directions: up(U), down(D), left(L), and right(R).

# 1 represents an open cell through which the rat can move.
# 0 represents a blocked cell that cannot be traversed.
# The rat can move only through open cells and cannot visit the same cell more than once in a path. Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat.

# Note: Return the paths in lexicographically increasing order. If no valid path exists, return an empty list.

# Examples:

# Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
# Output: ["DDRDRR", "DRDDRR"]
# Explanation: There are two valid paths from the source cell (0, 0) to the destination cell (3, 3).


class Solution:
  def rat(self, maze):
    n = len(maze)
    ans = []
    vis  =[[0 for _ in range(n)] for _ in range(n)]

    def findPath(i, j, a, n, ans, move, vis):
      if i == n-1 and j==n-1:
        ans.append(move)
        return 

      if i+1<n and not vis[i+1][j] and a[i+1][j] ==1:
        vis[i][j] = 1
        findPath(i+1, j, a, n, ans, move+"D", vis)
        vis[i][j] =0

      if j-1>=0 and not vis[i][j-1] and a[i][j-1] ==1:
        vis[i][j] =1
        findPath(i, j-1, a, n, ans, move+"L", vis)
        vis[i][j] = 0

      if j+1<n and not vis[i][j+1] and a[i][j+1] ==1:
        vis[i][j] =1
        findPath(i, j+1, a, n, ans, move+"R", vis)
        vis[i][j] =0

      if i-1>=0 and not vis[i-1][j] and a[i-1][j] ==1:
                vis[i][j] = 1
                findPath(i-1, j, a, n, ans, move+"U", vis)
                vis[i][j] = 0
    if maze[0][0] == 1:
      findPath(0, 0, maze, n, ans, "", vis)
    return ans