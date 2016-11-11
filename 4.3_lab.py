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