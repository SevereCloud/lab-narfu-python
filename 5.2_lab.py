def strHeap(arr):
	size = len(arr)
	if size == 0: return "<empty heap>"
	def recurse(i):
		if i > h.size: return [], 0, 0
		label = str(arr[i])
		left_lines, left_pos, left_width = recurse( i * 2)
		right_lines, right_pos, right_width = recurse( i * 2 + 1)
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
		lines = [' ' * left_pos + label + ' ' * (right_width - right_pos), ' ' * left_pos + '/' + ' ' * (middle-2) + '\\' + ' ' * (right_width - right_pos)] + [left_line + ' ' * (width - left_width - right_width) + right_line
		for left_line, right_line in zip(left_lines, right_lines)]
		return lines, pos, width
	return '\n'.join(recurse(1) [0])




import time
import random

class Heap:
	def __init__(self):
		self.heap_list= [0]
		self.size = 0

	def extract_min(self):
		r = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.size]
		self.size = self.size - 1
		self.heap_list.pop()
		i = 1
		while (i * 2) <= self.size:
			mc = self.min_child(i)
			if self.heap_list[i] > self.heap_list[mc]:
				tmp = self.heap_list[i]
				self.heap_list[i] = self.heap_list[mc]
				self.heap_list[mc] = tmp
			i = mc
		return r

	def min_child(self,i):
		if i * 2 + 1 > self.size:
			return i * 2
		else:
			if self.heap_list[i*2] < self.heap_list[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def build_heap(self, l):
		self.size = len(l)
		self.heap_list+=self.heap(l)

	def heap(self, l):
		size = len(l)-1

		for i in range(size, -1, -1):
			if 2*i+1<=size:
				if l[i]>l[2*i+1]:
					l[i],l[2*i+1] = l[2*i+1], l[i]
			if 2*i+2<=size:
				if l[i]>l[2*i+2]:
					l[i],l[2*i+2] = l[2*i+2], l[i]
	
		return l


	def __str__(self):
		if self.size == 0: return "<empty heap>"
		def recurse(h,i):
			if i > h.size: return [], 0, 0
			label = str(h.heap_list[i])
			left_lines, left_pos, left_width = recurse(h, i * 2)
			right_lines, right_pos, right_width = recurse(h, i * 2 + 1)
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
			lines = [' ' * left_pos + label + ' ' * (right_width - right_pos), ' ' * left_pos + '/' + ' ' * (middle-2) + '\\' + ' ' * (right_width - right_pos)] + [left_line + ' ' * (width - left_width - right_width) + right_line
			for left_line, right_line in zip(left_lines, right_lines)]
			return lines, pos, width
		return '\n'.join(recurse(self, 1) [0])

s = 0
while s == 0:
	n = int(input ('\n size array '))
	arr = []
	for i in range(n): arr.append(random.randint(0, 100))

	h = Heap()
	h.build_heap(arr)
	print (h)
	for l in range(n):
		print (h.extract_min())
		print ()
		print (h)