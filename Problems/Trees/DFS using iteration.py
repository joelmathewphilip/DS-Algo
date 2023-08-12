L = []


def dfsIterationPreOrder(root):
    stack = []
    stack.append(root)
    while len(stack) > 0:
        temp = stack[-1]
        stack.pop(-1)
        L.append(temp.val)
        if temp:
            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=3)
node9 = TreeNode(val=9)
node20 = TreeNode(val=20)
node15 = TreeNode(val=15)
node7 = TreeNode(val=7)
root.left = node9
root.right = node20
node9.left = node15
node9.right = node7
L = []
dfsIterationPreOrder(root)
assert L == [3, 9, 15, 7, 20], "Incorrect Dfs using Iteration"
