
#	Построение дерева разбора для вычисления выражений
#
#	Пример исходных данных:
#	( 1 + ( 2 * 3 ) )
#	Для упрощения разбора можно использовать знак пробела
#	между символами.
#
#	Описание алгоритма:
#	1. Если текущий элемент '(', добавить новый узел в качестве
#	левого поддерева текущего узла и перейти к левому поддереву.
#
#	2. Если текущий элемент принадлежит списку операторов
#	['+','-','/','*'], тогда присвоить текущему узлу данный
# оператор. Добавить новое правое поддерево и перейти к нему.
#
#	3. Если текущий элемент число, тогда присвоить текущему узлу
#	значение данного числа и перейти к родительскому узлу.
#
#	4. Если текущий элемент ')', тогда перейти к родительскому узлу.
#
# Пример работы алгоритма для выражения (1 + (2 * 3)):
#	1. Создать пустое дерево.
#	2. Использовать ( в качестве первого элемента. Согласно первому
#	пункту алгоритма создать левое поддерево и перейти к нему.
#	3. Следующий элемент: 1. Согласно 3 пункту присвоить текущему
#	узлу значение 1 и вернуться к родительскому узлу.
#	4. Следующий элемент:	+. Согласно	2 пункту,	присвоить	'+'	текущему
#	узлу. Добавить правое	поддерево и	перейти к	нему.
#	5. Следующий элемент:	(. Согласно 1 пункту создать левое поддерево
#	и перейти к нему.
#	б. Следующий элемент: 2. Согласно 3 пункту присвоить текущему
#	узлу значение 2 и вернуться к родительскому узлу.
#	7. Следующий элемент:	*. Согласно	2 пункту,	присвоить	'*'	текущему
#	узлу. Добавить правое	поддерево и	перейти к	нему.
#	8. Следующий элемент: 3. Согласно 3 пункту присвоить текущему
#	узлу значение 3 и вернуться к родительскому узлу.
#	9. Следующий элемент: ). Согласно 4 пункту переходим к
#	родительскому узлу узла *.
#	10. Следующий элемент: ). Согласно 4 пункту переходим к
#	родительскому узлу узла +. Т.к. больше родителей больше нет,
#	алгоритм завершен.


class BinaryTree:
    def __init__(self,rootNode):
        self.root = rootNode
        self.left = None
        self.right = None

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


def buildExprTree(s):
    expr = s.split()
    # Используем список stack в качестве стека для возврата к
    # родителю текущего узла. Для этого используем методы списка
    # append() и pop()
    stack = []
    tree = BinaryTree('')
    stack.append(tree)
    currentTree = tree
    for i in expr:
        if i == '(':
            tree.currentTree.insertLeft('')
            stack.append(currentTree)
            currentTree = tree.currentTree.getLeftChild()
            
        elif i not in ['+', '-', '*', '/', ')']:
            tree.currentTree.setRoot(i)
            
            currentTree = tree.currentTree.getLeftChild()
            stack.append(currentTree)

            currentTree = stack.pop()
        elif i in ['+', '-', '*', '/']:
            tree.setRoot(i)
            tree.insertRight('')
            tree = tree.getRightChild()
        elif i == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

t = buildExprTree("( ( 9 + 3 ) * 6 )")