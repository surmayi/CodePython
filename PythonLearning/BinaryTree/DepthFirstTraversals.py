class Node:
    def __init__(self,data):
        self.data= data
        self.left =None
        self.right= None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,node):
        if node:
            print(node.data, end='-')
            self.preorder(node.left)
            self.preorder(node.right)
        return

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data, end='-')
            self.inorder(node.right)
        return

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end='-')
        return

    def traverse(self,method='preorder'):
        if method=='postorder':
            self.postorder(self.root)
            return
        if method=='inorder':
            self.inorder(self.root)
            return
        self.preorder(self.root)
        return


# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.traverse("preorder"))
print(tree.traverse("inorder"))
print(tree.traverse("postorder"))