import random
import operator

class BinaryTree:

    def __init__(self, rootNode):
        self.root = rootNode
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
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

    def setRoot(self, obj):
        self.root = obj

    def __str__(self):
        self.i = 0
        def dis(obj):
            t =''
            
            ii = self.i

            if obj.left != None:
                self.i += 1
                t += dis(obj.left)

            t += ('.'*ii)+str(obj.root) +'\n'

            self.i = ii
            if obj.right != None:
                self.i += 1
                t +=dis(obj.right)
            return t

        return str(dis(self))


def buildExprTree(s):
    expr = s.split()
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

    def __init__(self, tree):
        self.result = self.count(tree)

    def operation(self, o, l, r):
        opers = {'+': operator.add, '-': operator.sub,
                 '*': operator.mul, '/': operator.truediv}
        f = opers[o]
        return f(l, r)

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

        return self.operation(o, l, r)

    def __str__(self):
        return self.result


class randomExpr():

    def __init__(self):
        self.o = [' + ', ' - ',  ' * ', ' / ']
        self.s = ''
        self.ops = random.randint(1, 10)
        self.op = self.ops
        self.path = 0
        self.currentpath = 0
        self.exp()

    def __str__(self):
        return self.s

    def exp(self):
        self.s += '( '
        self.path += 1
        self.currentpath += 1

        if self.op > 1 and self.ops > self.path:
            if random.randint(0, 1) == 0:
                self.number()
                self.operator()
            else:
                self.exp()
                self.operator()
        else:
            self.number()
            self.operator()

        self.s += ' )'
        self.currentpath -= 1

    def number(self):
        self.s += str(random.randint(1, 50))

    def operator(self):
        self.s += self.o[random.randint(0, len(self.o) - 1)]
        self.op -= 1

        if self.ops == self.path or self.op == 1:
            self.number()
        else:
            self.exp()

s = 0
while s == 0:
    t = randomExpr()
    print (t)
    tt = buildExprTree(str(t))
    exec ('result =' + str(t))
    print (tt) 
    print (evalExprTree(tt).result)
    
    assert (evalExprTree(tt).result == result)
