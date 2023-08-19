from collections import defaultdict


class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        redPath = defaultdict(list)
        bluePath = defaultdict(list)
        for i, j in redEdges:
            redPath[i].append(j)
        for i, j in blueEdges:
            bluePath[i].append(j)
        queue = [[0, -1, 0]]
        visited = set()
        # blue = 0 red = 1
        finalResult = [-1 for i in range(0, n)]
        finalResult[0] = 0
        # print(finalResult)
        while len(queue) > 0:
            length = len(queue)
            for i in range(0, length):
                node, color, distance = queue.pop(0)
                # print(node,color,distance)
                if (node, color) in visited:
                    continue
                visited.add((node, color))
                if finalResult[node] == -1:
                    finalResult[node] = distance
                # print(finalResult)
                if node == 0:
                    if node in bluePath:
                        for j in range(0, len(bluePath[node])):
                            queue.append([bluePath[node][j], 1, distance+1])
                    if node in redPath:
                        for j in range(0, len(redPath[node])):
                            queue.append([redPath[node][j], 0, distance+1])
                else:
                    if color == 0:
                        if node not in bluePath:
                            continue
                        else:
                            for j in range(0, len(bluePath[node])):
                                queue.append(
                                    [bluePath[node][j], 1, distance+1])
                    else:
                        if node not in redPath:
                            continue
                        else:
                            for j in range(0, len(redPath[node])):
                                queue.append([redPath[node][j], 0, distance+1])
                # print(queue)
        return finalResult


obj = Solution()
# print(obj.shortestAlternatingPaths(
#     n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]))
assert obj.shortestAlternatingPaths(
    n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]) == [0, 1, -1], "Incorrect"
