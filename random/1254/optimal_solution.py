# Pretty much just copy pasted the solution from Neetcode
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return False

            if grid[i][j] == 1 or (i, j) in visited:
                return True

            visited.add((i, j))

            return min(dfs(i + 1, j), dfs(i - 1, j), dfs(i, j + 1), dfs(i, j - 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and not grid[i][j]:
                    if dfs(i, j):
                        res += 1

        return res
