"""
test case:
18
insert 8
insert 2
insert 3
insert 7
insert 22
insert 1
find 1
find 2
find 3
find 4
find 5
find 6
find 7
find 8
print
delete 2
delete 7
print
"""

class BinarySearchtree:

    class BinaryNode:
        def __init__(self, key: int):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
    
    def insert(self, key: int):
        x = self.root #Treeの根
        y = None #xの親
        z = self.BinaryNode(key)
        
        # ノードzの親を検索する
        while x is not None:
            y = x #xがNoneではなかったら親ノードyをxに変更する
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        
        z.parent = y #zの親をyとする。初回はNoneになる
        if y == None:
            self.root = z 
        else: #親yから見たノードzを登録
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    # 同じキーを持つノード
    def find(self, key: int):
        x = self.root
        while (x is not None) and (key is not x.key):
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # 後継者を見つける
    def findSuccessor(self, node: BinaryNode):
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        #↓これがなんのためにいるのか不明
        parent = node.parent
        while(parent is not None) and (node is parent.right):
            node = parent
            parent = parent.parent
        return parent

    def delete(self, key: int):
        node = self.find(key)
        if node is None:
            print("Key: "+str(key)+" couldn't be found.")
            return
        
        if (node.left is None) or (node.right is None):
            target = node
        else:
            #nodeに二つの子がいる場合 中間順巡回でnodeの次に当たるノードがtargetになる
            target = self.findSuccessor(node) 

        if target.left is not None:
            child = target.left
        else:
            child = target.right

        if child is not None:
            child.parent = target.parent
        
        if target.parent is None:
            self.root = child
        else:
            if target.parent.left is target:
                target.parent.left = child
            else:
                target.parent.right = child
        
        if target is not node:
            node.key = target.key #keyだけ書き換えてnodeは使いまわし
        print()

    def inorder(self, n: BinaryNode):
        if n is None: return
        self.inorder(n.left)
        print(str(n.key)+" ", end="")
        self.inorder(n.right)
        return

    def preorder(self, n: BinaryNode):
        if n is None: return
        print(str(n.key)+" ", end="")
        self.preorder(n.left)
        self.preorder(n.right)
    
    def printInorder(self):
        self.inorder(self.root)
        print("")

    def printPreorder(self):
        self.preorder(self.root)
        print("")


if __name__ == '__main__':
    n = int(input())
    bst = BinarySearchtree()

    for i in range(n):
        line = input().split()
        com = line[0]
        if len(line) > 1: key = int(line[1])

        if com == "insert":
            bst.insert(key)

        elif com == "find":
            if bst.find(key) is None:
                print(str(key) + " couldn't be found")
            else:
                print(str(key) + " is found!")

        elif com == "delete":
            bst.delete(key)

        elif com == "print":
            bst.printInorder()
            bst.printPreorder()