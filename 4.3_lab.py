import random

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


class randomExpr():
	def __init__(self):
		self.o = ['+', '-',  '*', '/']
		self.s = ''
		self.i = random.randint(2, 10)
		if random.randint(0, 1) == 0:
			self.num()
		else:
			self.part()


	def num(self):
		self.s += str(random.randint(1, 50))
		self.i -= 1

		if self.i > 0:
			self.operator()

	def part(self):
		self.s += '('
		self.num()
		self.s += ')'

		if self.i > 0:
			self.operator()

	def operator(self):
		self.s += self.o [random.randint(0, len(self.o)-1)]

		if self.i == 1:
			self.num()
		else:
			r = random.randint(0, 2)
			if r == 0:
				self.num()
			elif r == 1:
				self.part()
			else:
				self.s += str(random.randint(1, 50))
				self.i -= 1



t = buildExprTree("( ( 9 + 3 ) * 6 )")

for i in range(50):
	print randomExpr().s
