from collections import defaultdict


class Solution:
    def Dfs(self, node, adjList):
        self.visited[node] = True
        # print(self.visited)
        for j in range(0, len(adjList[node])):
            if not self.visited[adjList[node][j]]:
                Solution.Dfs(self, adjList[node][j], adjList)

    def countComponents(self, n: int, edges) -> int:
        self.visited = [False for i in range(0, n)]
        adjList = defaultdict(list)
        for i in range(0, n):
            temp = []
            for j in range(0, len(edges)):
                if edges[j][0] == i:
                    adjList[edges[j][1]].append(edges[j][0])
                    adjList[i].append(edges[j][1])
            # adjList[i] = temp
        # print(adjList)
        count = 0
        for i in range(0, n):
            if not self.visited[i]:
                Solution.Dfs(self, i, adjList)
                count += 1
        return count


obj = Solution()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
assert obj.countComponents(
    n=n, edges=edges) == 1, "Incorrect no of connected components"
n = 2
edges = [[1, 0]]
assert obj.countComponents(
    n=n, edges=edges) == 1, "Incorrect no of connected components"
