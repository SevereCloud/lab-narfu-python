import operator


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

class evalExprTree:
    def __init__(self,tree):
        self.result = self.count(tree)

    def operation(self,o,l,r):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul,'/':operator.truediv}
        f = opers[o]
        return f(l,r)


    def count(self, tree):
        o = tree.root
        try:
            l = int(tree.getLeftChild().root)
        except ValueError:
            l = self.count(tree.getLeftChild())

        try:
            r = int(tree.getRightChild().root)
        except ValueError:
            r = self.count(tree.getRightChild())
        
        return self.operation(o,l,r)

    def __str__(self):
        return self.result


t = buildExprTree("( ( 9 + 3 ) * 6 )")
print (evalExprTree(t).result)