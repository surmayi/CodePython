class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BST:

    def __init__(self,data):
        self.root= Node(data)

    def insertNode(self,data):
        self.insertHelper(self.root,data)

    def insertHelper(self,node,data):
        if node.data>data:
            if node.left:
                self.insertHelper(node.left,data)
            else:
                node.left=Node(data)
                return
        else:
            if node.right:
                self.insertHelper(node.right,data)
            else:
                node.right=Node(data)
                return

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data, end='-')
            self.inorder(node.right)
        return

    def traverse(self,method='preorder'):
        if method=='inorder':
            self.inorder(self.root)
        return

    def searchNode(self,data):
        return self.searchHelper(self.root,data)


    def searchHelper(self,node,data):
        if node and node.data==data:
            return True
        elif node and node.data>data:
                return self.searchHelper(node.left,data)
        elif node:
            return self.searchHelper(node.right,data)
        return False


# Set up tree:
tree = BST(10)
tree.insertNode(3)
tree.insertNode(13)
tree.insertNode(23)
tree.insertNode(8)
tree.insertNode(1)
tree.insertNode(7)


print(tree.searchNode(1))
