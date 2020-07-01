class node:
	def __init__(self,value = None):
		self.value = value 
		self.next = None

class circularLinkedList:
	def __init__(self):
		self.root = None 
		self.size = 0

	def insert(self,value):
		if self.size == 0:
			self.root = node(value)
			self.root.next = self.root 
		else:
			newNode = node(value)
			curNode = self.root
			while curNode.next != self.root:
				curNode = curNode.next
			curNode.next = newNode
			newNode.next = self.root
		self.size += 1

	
	def delete(self,value):
		curNode = self.root 
		prevNode = None 
		while True:
			if curNode.value == value:
				if prevNode != None:
					prevNode.next = curNode.next
				else:
					while curNode.next != self.root:
						curNode = curNode.next
					curNode.next = self.root.next
					self.root = self.root.next
				self.size -= 1
				return True
			elif curNode.next == self.root:
				return False 
			prevNode = curNode
			curNode = curNode.next
		

	def printList(self):
		if self.root == None:
			return 
		curNode = self.root
		print(curNode.value) 
		while curNode.next != self.root:
			curNode = curNode.next 
			print(curNode.value)
	
	
	def search(self,value):
		curNode = self.root 
		while True:
			if curNode.value == value:
				return True 
			elif curNode.next == self.root:
				return False 
			curNode = curNode.next 
		


#Driving code for graph-based algorithms
#Uncomment to test
"""
g = Graph()
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')
vertices = [a,b,c,d,e,f]
for vertex in vertices:
	g.addVertex(vertex)
g.addEdge('a', 'b', 7)  
g.addEdge('a', 'c', 9)
g.addEdge('a', 'f', 14)
g.addEdge('b', 'c', 10)
g.addEdge('b', 'd', 15)
g.addEdge('c', 'd', 11)
g.addEdge('c', 'f', 2)
g.addEdge('d', 'e', 6)
g.addEdge('e', 'f', 9)
for v in g.vertices:
	print(v)
	print(g.vertices[v].color)
	print(g.vertices[v].distance)
	print("\n")
print("After doing a Breadth-First Search from Vertex A:")
g.bfs(a)
for v in g.vertices:
	print(v)
	print(g.vertices[v].color)
	print(g.vertices[v].distance)
	print("\n")
g.resetGraph()
path = ['d']
Djikstra(g,a)
shortest(d,path)
print(path)

"""
#Compare the quick sort times

"""
from time import time 
from random import randint,shuffle
arr = [i for i in range(1,10001)]
arr = sorted(arr,reverse = True)
t1 = time()
mergeSort(arr)
mergeTime = time() - t1
print("Time taken for Merge sorting:")
print(mergeTime)

arr = sorted(arr,reverse = True)
t1 = time()
a = quickSort(arr)
quickTime = time() - t1
print("Time taken for Quick sorting:")
print(quickTime)
"""

#Driving code for twos compliment
"""
from time import time
arr = [i for i in range(-40,-30)]
twosArray = []
t1 = time()
for a in arr:
	twosArray.append(getTwosCompliment(a))
t = time() - t1
print("Two's compliment for my method:")
print(t)

twosArray = []
t1 = time()
for a in arr:
	twosArray.append(twos_comp(a,8))
t = time() - t1
print("Two's compliment for the other method:")
print(t)
"""


#Driver code for Heap - Min and Max
"""
bh = minHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
print(bh.deleteMin())
"""

#Driver code for Circular Linked list
#Uncomment to test

mL = circularLinkedList()
mL.insert(1)
mL.insert(2)
mL.insert(3)
mL.insert(4)
mL.insert(5)
mL.insert(6)
mL.printList()
print("\n")
	mL.delete(4)
mL.printList()
print("\n")
print(mL.search(4))
print(mL.search(7))
print("\n")
print(mL.root.value)







