from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self,ch):
        return ord(ch)==ord('a')

    def insert(self,key):
        if key is None:
            return
        key =key.lower()
        level =0
        cur=self.root
        for ind in range(len(key)):
            level = self.getIndex(key[ind])
            if cur.children[level] is None:
                cur.children[level] = TrieNode(key[ind])
                print(key[ind], 'inserted')
            cur=cur.children[level]
        print(key, 'inserted')
        cur.set_end_word()


    def search(self,key):
        if key is None:
            return False
        cur = self.root
        index =0
        key = key.lower()

        for ind in range(len(key)):
            index = self.getIndex(key[ind])
            if cur and cur.children[index] is None:
                return False
            cur=cur.children[index]
        if cur and cur.is_end_word == True:
            return True
        return False

    def hasNoChildren(self,node):
        for ind in range(len(node.children)):
            if node.children[ind] is not None:
                return False
        return True

    def delete(self,key):
        if key is None or self.root is None:
            return False
        self.deleteHelper(key,self.root,len(key),0)

    def deleteHelper(self,key,curNode,length,begin):

        deleted_self= False
        if curNode is None:
            return deleted_self
        if length==begin:
            if self.hasNoChildren(curNode):
                deleted_self=True
                curNode=None
            else:
                curNode.reset_end_word()
                deleted_self=False
        else:
            print('checking for ' + key[begin])
            childNode= curNode.children[self.getIndex(key[begin])]
            child_deleted= self.deleteHelper(key,childNode,length,begin+1)
            if child_deleted:
                curNode.children[self.getIndex(key[begin])]=None
                if curNode.is_end_word():
                    deleted_self=False

                elif self.hasNoChildren(curNode) is False:
                    deleted_self=False
                else:
                    curNode = None
                    deleted_self=True

            else:
                deleted_self= False
        return deleted_self



keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i])

if t.search("the") is True:
    print("the --- " + output[1])
else:
    print("the --- " + output[0])

if t.search("these") is True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])

t.delete("abc")
print("Deleted key \"abc\"")

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])

print(t.delete('bye'))
print(t.search('bye'))