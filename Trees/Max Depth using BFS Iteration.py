
def maxDepth(root) -> int:
    #iterative DFS approach
    depth = 1
    L = []
    L = [[root,1]]
    maxDepth = -1
    while len(L) > 0:
        print(list(map(lambda x,y:(x[0].val,y[1]),L,L)))
        temp = L[0]
        #if not temp[0].left and not temp[0].right:
        maxDepth = max(maxDepth,temp[1])
        if temp[0].left:
            value = [temp[0].left,temp[1] + 1]
            L.append(value)
        if temp[0].right:
            value = [temp[0].right,temp[1] + 1]
            L.append(value)
        L.pop(0)
    return maxDepth



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
node9.right = node7

# root.right = node20
# node20.left=node15
# node20.right=node7

print(maxDepth(root = root))


