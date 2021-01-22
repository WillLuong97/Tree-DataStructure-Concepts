#Problem 559. Maximum Depth of N-ary Tree

'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 
Example 1:
Input: root = [1,null,3,2,4,null,5,6] 1: [3,2,4]; 3: [5,6]; 2:[5,6]; 4: [5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
 

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 104].
'''
#Tree node structure
class Node():
	def __init__(self, data):
		self.data = data
		self.children = []
	
	def addChildrenToNode(self, obj):
		self.children.append(obj)

	def printNode(self):
		#base case: 
		if not self.data:
			return ""
		print(self.data)
		for child in self.children:
			print(child.data)

def maxDepth(root):
	#base case: empty tree
	if not root: 
		return 0
	treeDepth = 0 #level
	#Queue to store each tree node in a level, at level 0, we put the root node in 
	queue = [root]
	while queue:
		#looping through the level of the queue:
		for _ in range(len(queue)):
			current_node = queue.pop()
			#if the current node still has children then 
			#it is not a leaf node, so we move to the next level and add its nodes onto the queue
			if current_node.children:
				for child in current_node.children:
					queue.append(child)
		treeDepth += 1

	return treeDepth




#Main function to run the test cases: 
def main():
	print("TESTING MAXIMUM DEPTH N-ARY TREE...")
	#creating a tree with tree node
	#[1,null,3,2,4,null,5,6] 	
	root = Node(1)
	first_left = Node(3)
	first_right = Node(2)
	first_right_right = Node(4)
	second_left = Node(5)
	second_right = Node(6)
	root.addChildrenToNode(first_left)
	root.addChildrenToNode(first_right)
	root.addChildrenToNode(first_right_right)
	root.addChildrenToNode(second_left)
	root.addChildrenToNode(second_right)
	print(maxDepth(root))
	print("END OF TESTING...")
	
main()
