def maxDepth(root):
    if not root:
        return 0
    if root.left:
        return 1 + maxDepth(root.left)
    if root.right:
        return 1 + maxDepth(root.right)
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=3)
node9 = TreeNode(val = 9)
node20 = TreeNode(val = 20)
node15 = TreeNode(val = 15)
node7 = TreeNode(val=7)
root.left = node9
root.right = node20
node9.left = node15
node15.right = node7

# root.right = node20
# node20.left=node15
# node20.right=node7

print(maxDepth(root = root))