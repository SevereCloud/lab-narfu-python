
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
    
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.root)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos), ' ' * left_pos + '/' + ' ' * (middle-2) + '\\' + ' ' * (right_width - right_pos)] + [left_line + ' ' * (width - left_width - right_width) + right_line for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self) [0])


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
            currentTree.insertLeft('')
            stack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRoot(i)
            currentTree = stack.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRoot(i)
            currentTree.insertRight('')
            stack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

t = buildExprTree("( ( 9 + 3 ) * 6 )")

print (t)