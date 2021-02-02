class Node:
    def __init__(self,data):
        self.data= data
        self.left =None
        self.right= None

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,node):
        self.items.insert(0,node)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def peek(self):
        return self.items[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,node):
        self.items.append(node)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


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

    def levelOrder(self,node):
        if node is None:
            return
        queue =Queue()
        queue.enqueue(node)
        while len(queue)>0:
            node = queue.dequeue()
            print(node.data,end='->')
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return

    def reverseLevelOrder(self, node):
        if not node:
            return
        queue =Queue()
        queue.enqueue(node)
        stack = Stack()
        while len(queue)>0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while stack.peek():
            print(stack.pop().data,end='->')

    def traverse(self,method='preorder'):
        if method=='postorder':
            self.postorder(self.root)
            return
        if method=='inorder':
            self.inorder(self.root)
            return
        if method=='levelorder':
            self.levelOrder(self.root)
            return
        if method=='reverselevelorder':
            self.reverseLevelOrder(self.root)
            return
        self.preorder(self.root)
        return

    def heightOfTree(self,node):
        if not node:
            return -1
        left = self.heightOfTree(node.left)
        right = self.heightOfTree(node.right)

        return 1 + max(left,right)




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
tree.root.right.right.right = Node(8)

print(tree.heightOfTree(tree.root))