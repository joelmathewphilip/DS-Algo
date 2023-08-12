from collections import defaultdict


class Solution:
    def Dfs(self, adjList, node, destination):
        self.visited[node] = True
        if node == destination:
            return True
        for i in range(0, len(adjList[node])):
            if self.visited[adjList[node][i]] == False:
                if Solution.Dfs(self, adjList, adjList[node][i], destination) == True:
                    return True

    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        self.visited = [False for i in range(0, n)]
        self.reachable = False
        adjList = defaultdict(list)
        for i in range(0, len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])

        # print(adjList)
        if Solution.Dfs(self, adjList, source, destination) == True:
            return True
        else:
            return False


edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4],
         [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
n = 10
source = 5
destination = 9
obj = Solution()
assert obj.validPath(n=n, edges=edges, source=source,
                     destination=destination) == True, "Output should be True"
