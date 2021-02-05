#Problem 872. Leaf-Similar Trees

'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
'''
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


#Tree Traversal Recursively
def leafSimilar(root1, root2):
	#helper method to recursively traverse a tree
	def dfs(root, leaf):
		if root:
			#if the current node is a leaf node then we will add it onto the leaves
			#since the two tree are traversed using the same graph, the leaf sequence should be the same 
			if not root.left and not root.right:
				leaf.append(root.val)
			dfs(root.left, leaf)
			dfs(root.right, leaf)
	

	leaf1 = []
	dfs(root1, leaf1)
	leaf2 = []
	dfs(root2, leaf2)
	return leaf1 == leaf2

#Iterative methods
def leafSimilar_ITERATIVE(root1, root2):
	#helper method to traverse the tree iteratively
	def dfs_iter(root):
		#leaves store all the leaf node from the tree
		leaves = []
		#keep track of all the node as we move through the tree
		stack = []
		#inorder traversal: 
		while stack or root:
			#if root exist, then push element onto the stack 
			if root:
				stack.append(root)
				root = root.left
				
			#if there is no more root to look for: then we pop element out from the stack and check to see which ones is a leaf node
			else:
				root = stack.pop()
				#if the current node is a leaf node
				if not root.left and not root.right:
					leaves.append(root.val)
				#if the current node has a right child then the above if statement will be true again and then the right child gets appended to the stack
				root = root.right
		return leaves
	return dfs_iter(root1) == dfs_iter(root2)
	
#Main function to run the test case:
def main():
	print("TESTING LEAF-SIMILAR TREES...")
	#create a tree:
	root1 = TreeNode(3)
	root1.left = TreeNode(5)
	root1.left.left = TreeNode(6)
	root1.left.right = TreeNode(2)
	root1.left.right.left = TreeNode(7)
	root1.left.right.right = TreeNode(4)
	root1.right = TreeNode(1)
	root1.right.left = TreeNode(9)
	root1.right.right = TreeNode(8)
 
	root2 = TreeNode(3)
	root2.left = TreeNode(5)
	root2.left.left = TreeNode(6)
	root2.left.right = TreeNode(2)
	root2.left.right.left = TreeNode(7)
	root2.left.right.right = TreeNode(4)
	root2.right = TreeNode(1)
	root2.right.left = TreeNode(9)
	root2.right.right = TreeNode(8)
 	
	print(leafSimilar(root1, root2))
	print(leafSimilar_ITERATIVE(root1, root2))
	print("END OF TESTING...")

main()


