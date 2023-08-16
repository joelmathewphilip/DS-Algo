# Definition for a binary tree node.
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildGraph(self, node, parent):
        if not node:
            return
        if node.left:
            self.hashMap[node.left.val] = node
            Solution.buildGraph(self, node.left, node)
        if node.right:
            self.hashMap[node.right.val] = node
            Solution.buildGraph(self, node.right, node)

    def Dfs(self, node, distance, target):
        if not node:
            return
        if node.val in self.visited:
            return
        if distance == target:
            self.elements.append(node.val)
            return
        self.visited.add(node.val)
        if node.left:
            Solution.Dfs(self, node.left, distance+1, target)
        if node.right:
            Solution.Dfs(self, node.right, distance+1, target)
        if node.val in self.hashMap:
            Solution.Dfs(self, self.hashMap[node.val], distance+1, target)

    def distanceK(self, root, target, k):
        self.hashMap = {}
        self.visited = set()
        self.elements = []

        Solution.buildGraph(self, root, None)
        Solution.Dfs(self, target, 0, k)
        # print(self.elements)
        return self.elements


obj = Solution()
root3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)
root3.left = node5
root3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4
assert obj.distanceK(root=root3, target=node5, k=2) == [
    7, 4, 1], "Incorrect Value"
