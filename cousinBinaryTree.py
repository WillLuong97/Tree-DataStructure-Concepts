#Problem 993. Cousins in Binary Tree

'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''
#Definition of a binary tree
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def isCousins(root, x, y):
	#to keep track of which node currently in the level
	parent = {root.val: (None, 0)} #node: [parent, level]
	stack = [] #to keep track of the current tree node
	level = 0 
	stack.append(root)
	while stack:
		#go through each level to find the node value
		size = len(stack)
		level += 1
		for i in range(size):
			node = stack.pop(0)
			if node.left:
				parent[node.left.val] = (node.val, level)
				stack.append(node.left)
			if node.right:
				parent[node.right.val] = (node.val, level)
				stack.append(node.right)
	#true if the 
	return parent[x][0] != parent[y][0] and parent[x][1] == parent[y][1]
	

	



#Main function to run the test cases:
def main():
	print("TESTING COUSINS IN BINARY TREE PROBLEM...")
	root = TreeNode(1)
	two = TreeNode(2)
	three = TreeNode(3)
	four = TreeNode(4)
	root.left = two
	root.right = three
	two.right = four
	x = 4
	y = 3

	print(isCousins(root, x, y))
	print("END OF TESTING...")

main()

