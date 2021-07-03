#Finding the Inorder successor of a binary search tree

'''
Given a Binary Search Tree, find the inroder traversal of a target node in the current tree 

In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. Inorder Successor is NULL for the last node in Inorder traversal. 
In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the smallest key greater than the key of the input node. So, it is sometimes important to find next node in sorted order.

'''

#Tree Node class 
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solutions:
	#Helper method to find the node of the target int
	def findTarget(self, root, target):
		if not root:
			return None
		#traverse the tree until we find the target node using dfs
		if root.val == target:
			return root 
		#since this is a bst, we can apply binary search to find the target for a more efficient apparoach
		elif root.val < target:
			return self.findTarget(root.right, target)
		
		else: 
			return self.findTarget(root.left, target)

	#Helper method to find the leftmost element in the tree 
	def leftMostNode(self, node):
		#base case: the sub tree is empty, then we will return none
		if not node:	
			return 
		current = node 
		while(current.left != None):
			current = current.left
		return current
	#Output: TreeNode  
	def FindInorderSuccessor(self, root, target):
		#base case: return null if the tree is empty 
		if not root: 
			return None
		#Find the target value as a tree node in the tree
		target_node = self.findTarget(root, target)
		#if target is not from the tree
		if(target_node == None):
			return None	
		#CASE 1: the target node has a right subtree, so the inorder successor would be the left most element in that substree 
		if(target_node.right != None):
			return self.leftMostNode(target_node.right)
		
		else: 
			#CASE 2: the target node does not have a right subtree, so we will have to backtrack to its parents node to find the inorder successor 
			print("CASE 2 IS CALLED!")
			successor = None
			parent = root
			while(parent != target_node):
				if(target_node.val < parent.val):
					#then we might have found our inorder successor 
					successor = parent
					parent = parent.left
				else:
					parent = parent.right
		return parent
#Main function to test the program
def main():
	print("TESTING INORDER SUCCESSOR OF A BINARY SEARCH TREE...")

	#Test tree: 
	root = TreeNode(20)
	root.left = TreeNode(8)
	root.right = TreeNode(22)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(12)
	root.left.right.left = TreeNode(10)
	root.left.right.right = TreeNode(14)

	findInorder = Solutions()
	print(findInorder.FindInorderSuccessor(root, 8).val)

	print("END OF TESTING...")

main()
