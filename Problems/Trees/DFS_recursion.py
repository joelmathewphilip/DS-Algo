L = []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrderTraverseTree(root):
    if not root:
        return
    L.append(root.val)
    preOrderTraverseTree(root.left)
    preOrderTraverseTree(root.right)
    return


def inOrderTraverseTree(root):
    if not root:
        return
    preOrderTraverseTree(root.left)
    L.append(root.val)
    preOrderTraverseTree(root.right)
    return


def postOrderTraverseTree(root):

    if not root:
        return
    preOrderTraverseTree(root.left)
    preOrderTraverseTree(root.right)
    L.append(root.val)
    return


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
preOrderTraverseTree(root)
assert L == [
    3, 9, 15, 7, 20], "PreOrder traversal is incorrect"

L = []
inOrderTraverseTree(root)
assert L == [
    9, 15, 7, 3, 20], "Inorder Traversal is incorrect"

L = []
postOrderTraverseTree(root)
assert L == [
    9, 15, 7, 20, 3], "Post Order Traversal is incorrect"
