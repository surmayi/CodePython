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

    def getInorderList(self,node,lis=[]):
        if node:
            self.getInorderList(node.left,lis)
            lis.append(node.data)
            self.getInorderList(node.right,lis)
        return lis

    def checkIfBST(self):
        lis = self.getInorderList(self.root)
        for i in range(0,len(lis)-1):
            if lis[i]>lis[i+1]:
                return False
        return True


# Set up tree:
tree = BST(10)
tree.insertNode(3)
tree.insertNode(13)
tree.insertNode(23)
tree.insertNode(8)
tree.insertNode(1)
tree.insertNode(7)

print(tree.checkIfBST())