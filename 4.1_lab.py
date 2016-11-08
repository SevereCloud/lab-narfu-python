# File: BinaryTree.py
# Реализация бинарных деревьев
# Пример использования класса:

# t = BinaryTree('root')
# print(t.getRoot())
# print(t.getLeftChild())

# t.insertLeft('left')
# print(t.getLeftChild())
# print(t.getLeftChild().getRoot())

# t.insertRight('right')
# print(t.getRightChild())
# print(t.getRightChild().getRoot())

# t.getRightChild().setRoot('right root')
# print(t.getRightChild().getRoot())

class BinaryTree:

# Метод __init__ вызывается каждый раз, когда создается объект
# данного класса. В этом методе мы инициализируем новый объект.
# У нашего класса три атрибута: root, left, right, которые могут
# ссылаться на другие экземпляры класса BinaryTree.

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
        pass # Реализуйте метод

    def getRoot(self):
        pass # Реализуйте метод

    def getRightChild(self):
        pass # Реализуйте метод

    def getLeftChild(self):
        pass # Реализуйте метод

    def setRoot(self,obj):
        pass # Реализуйте метод

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