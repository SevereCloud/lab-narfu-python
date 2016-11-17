
class BST:
    def __init__(self):
        self.root = None

    def insert(self, k):
        new = BSTnode(k)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if k < node.key:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, k):
        node = self.root
        while node is not None:
            if k == node.key:
                return node
            elif k < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def extarct_min(self):
        if self.root is None:
            return None
        else:
            node = self.root
            while node.left is not None:
                node = node.left
            if node.parent is not None:
                node.parent.left = node.right
            else: 
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            self.left = None
            self.right = None
            self.parent = None
            return node

    def left_rotate(self):


    def right_rotate(self):


    def rebalance(self):


    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
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
        return '\n'.join(recurse(self.root) [0])

class BSTnode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# Визуализация работы алгоритмов
def test():
    import random
    items = (random.randrange(100) for i in range(10))

    tree = BST()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)

test()