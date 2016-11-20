

class BinaryTree:
    def __init__(self,rootNode):
        self.root = rootNode
        self.left = None
        self.right = None

# Метод insertLeft используется для вставки левого поддерева в
# текущий узел. Обратите внимание что атрибуту left присваивается
# экземпляр класса BinaryTree.
# В методе рассматривается два случая: когда у узла нет левого
# поддерева, и когда поддерево уже существует.

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRoot(self):
        return self.root

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRoot(self,obj):
        self.root = obj 


    def draw(self):
        s = []
        self.i = 0
        self.ii = 0
        def dis(obj):
            s.append(str(obj.root))
            t = (' '*self.i)+str(obj.root) +':\n'
            self.i += 1
            ii = self.i
            if obj.left != None:
                t +=(' '*self.i)+ dis(obj.left)
                self.i = ii
            if obj.right != None:
                t +=(' '*self.i)+ dis(obj.right)
            return t

        return str(dis(self))

        


t = BinaryTree('root')
print(t.getRoot())
print(t.getLeftChild())

t.insertLeft('left')
print(t.getLeftChild())
print(t.getLeftChild().getRoot())

t.insertRight('right')
print(t.getRightChild())
print(t.getRightChild().getRoot())

t.getRightChild().setRoot('right root')
print(t.getRightChild().getRoot())

print(t.draw())