
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrderTraverseTree(root):
    if not root:
        return
    print(root.val,end=" ")
    preOrderTraverseTree(root.left)
    preOrderTraverseTree(root.right)
    return

def inOrderTraverseTree(root):
    if not root:
        return
    preOrderTraverseTree(root.left)
    print(root.val,end=" ")
    preOrderTraverseTree(root.right)
    return

def postOrderTraverseTree(root):

    if not root:
        return
    preOrderTraverseTree(root.left)
    preOrderTraverseTree(root.right)
    print(root.val,end=" ")
    return




root = TreeNode(val=3)
node9 = TreeNode(val = 9)
node20 = TreeNode(val = 20)
node15 = TreeNode(val = 15)
node7 = TreeNode(val=7)
root.left = node9
root.right = node20
node9.left = node15
node9.right = node7


print("Pre Order Traversal")
preOrderTraverseTree(root)
print("\nInorder Traversal")
inOrderTraverseTree(root)
print("\nPost Order Traversal")
postOrderTraverseTree(root)