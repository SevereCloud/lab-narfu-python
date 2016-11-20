

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

        


t = BinaryTree('root')
print(t.getRoot())
print(t.getLeftChild())

t.insertLeft('left')
print(t.getLeftChild())
print(t.getLeftChild().getRoot())

t.insertRight('right')
print(t.getRightChild())
print(t.getRightChild().getRoot())

t.getRightChild().insertLeft('right root')


print()
print(t)