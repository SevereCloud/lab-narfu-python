

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