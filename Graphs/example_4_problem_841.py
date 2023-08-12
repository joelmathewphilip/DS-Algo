# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. 
# However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.


#Solution:
# Use DFS or BFS to solve this problem.
# DFS solution:
# 1) Our entry point is 0. So we will call DFS function with node = 0
# 2) Inside the DFS function
#   a) set the node as visited
#   b) decrement the count of nodes to be visited
#   c) Find all neighbours of the current node and recursively perform DFS
# 3) Once we come out of DFS, if the count of nodes to be visited ==0, then all nodes can be visited, so return True.
# Otherwise return False


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        def DFS(node):
            for i in range(0,len(rooms[node])):
                if rooms[node][i] not in visited:
                    visited.add(rooms[node][i])
                    DFS(rooms[node][i])
            return visited
        visited={0}
        DFS(0)
        return len(visited) == len(rooms)


obj = Solution()
print(obj.canVisitAllRooms(rooms=[[1,3],[3,0,1],[2],[0]]))
