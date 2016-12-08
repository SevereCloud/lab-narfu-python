
class BST:
    """Вставить элемент с ключем k"""
    def __init__(self):
        self.root = None

    def insert(self, k):
        """Вставить элемент с ключем k"""
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
                        update_height(node.left)
                        update_height(node)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        update_height(node.right)
                        update_height(node)
                        break
                    node = node.right

        update_height(self.root)
        return new

    def find(self, k):
        """Ищет элемент"""
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

    def left_rotate(self, node):
        """Малый левый поворот"""
        tmp = node

        return_node = node.left
        return_node.parent = None

        tmp.left = return_node.right
        tmp.left.parent = tmp

        return_node.right = tmp
        return_node.right.parent = return_node

        update_height(return_node.right)
        update_height(return_node)

        return return_node


    def right_rotate(self, node):
        """Малый правый поворот"""
        tmp = node

        return_node = node.right
        return_node.parent = None

        tmp.right = return_node.left
        tmp.right.parent = tmp

        return_node.left = tmp
        return_node.left.parent = return_node

        update_height(return_node.left)
        update_height(return_node)

        return return_node



    def rebalance(self, node):
        A = node
        F = A.parent #allowed to be NULL
        if node.balance() == -2:
            if node.right.balance() <= 0:
                """Rebalance, case RRC """
                B = A.right
                C = B.right
                assert (not A is None and not B is None and not C is None)
                A.right = B.left
                if A.right:
                    A.right.parent = A
                B.left = A
                A.parent = B
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                update_height(A)
                update_height(B.parent)
            else:
                """Rebalance, case RLC """
                B = A.right
                C = B.left
                assert (not A is None and not B is None and not C is None)
                B.left = C.right
                if B.left:
                    B.left.parent = B
                A.right = C.left
                if A.right:
                    A.right.parent = A
                C.right = B
                B.parent = C
                C.left = A
                A.parent = C
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                update_height(A)
                update_height(B)
        else:
            #assert(node.balance() == +2)
            if node.left.balance() >= 0:
                B = A.left
                C = B.left
                """Rebalance, case LLC """
                assert (not A is None and not B is None and not C is None)
                A.left = B.right
                if (A.left):
                    A.left.parent = A
                B.right = A
                A.parent = B
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                update_height(A)
                update_height(B.parent) 
            else:
                B = A.left
                C = B.right
                """Rebalance, case LRC """
                assert (not A is None and not B is None and not C is None)
                A.left = C.right
                if A.left:
                    A.left.parent = A
                B.right = C.left
                if B.right:
                    B.right.parent = B
                C.left = B
                B.parent = C
                C.right = A
                A.parent = C
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if (F.right == A):
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                update_height(A)
                update_height(B)

    def __str__(self):
        if self.root is None:
            return '<empty tree>'

        def recurse(node):
            if node is None:
                return [], 0, 0
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
            if label[0] == '.':
                label = ' ' + label[1:]
            if label[-1] == '.':
                label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos), ' ' * left_pos + '/' + ' ' * (middle - 2) + '\\' + ' ' * (right_width - right_pos)] + [left_line + ' ' * (width - left_width - right_width) + right_line for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root)[0])


class BSTnode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    def balance(self):
        return (self.left.height if self.left else -1) - (self.right.height if self.right else -1)

def height(node):
    if node is None:
        return -1
    else:
        update_height(node)
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1
    if node.parent is None == False:
        update_height(node.parent)



def test():
    import random
    items = (random.randrange(100) for i in range(10))

    tree = BST()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)
    tree.rebalance(tree.root)
    print()
    print(tree)

test()
