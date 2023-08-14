from collections import defaultdict


class Solution:
    def Dfs(self, node, adjList):
        self.visited[node] = True
        self.count += 1
        for i in range(0, len(adjList[node])):
            if not self.visited[adjList[node][i]]:
                Solution.Dfs(self, adjList[node][i], adjList)
        return

    def reachableNodes(self, n: int, edges, restricted) -> int:
        self.visited = [False for i in range(0, n)]
        restricted1 = set()
        for i in restricted:
            self.visited[i] = True
        adjList = defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        self.count = 0
        self.visited[0] = True
        Solution.Dfs(self, 0, adjList)
        return self.count


edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]
n = 7
obj = Solution()
assert obj.reachableNodes(
    n=n, edges=edges, restricted=restricted) == 3, "Invalid No of Nodes"
