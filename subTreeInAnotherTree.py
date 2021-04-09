#Problem 572. Subtree of Another Tree
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2
Return false.
'''
#Tree Node data model:
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
'''
The idea is to use preorder to generate a list or string of node in the two tree and check to see if preorder of tree2 or t is in tree1 or not
'''	
def isSubtree(s, t):
	#helper method to perform preorder traversal 
	def preorder(node): # This will return a string with the preorder traversal of the tree
		#if the node is empty, the return "null"
		if not node:
			return "null"
		return ' ' + str(node.val) + " " + preorder(node.left) + " " + preorder(node.right)
	#getting the preorder traversal of the s and t tree
	tree_s_preorder = preorder(s)
	tree_t_preorder = preorder(t)
	return tree_t_preorder in tree_s_preorder

#main function to run the test program
def main():
	print("TESTING SUBTREE OF ANOTHER TREE...")
	root_s = TreeNode(3)
	root_t = TreeNode(4)
	four = TreeNode(4)
	one = TreeNode(1)
	two = TreeNode(2)
	five = TreeNode(5)
	root_s.left = four
	root_s.right = five
	four.left = one
	four.right = two
	root_t.left = one
	root_t.right = two	
	print(isSubtree(root_s, root_t))
			
					
		
	print("END OF TESTING...")

main()

