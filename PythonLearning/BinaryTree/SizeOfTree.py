class Node:
    def __init__(self,data):
        self.data= data
        self.left =None
        self.right= None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def treeSize(self,node):
        if not node:
            return 0
        return 1 + self.treeSize(node.left) + self.treeSize(node.right)

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(7)

print(tree.treeSize(tree.root))