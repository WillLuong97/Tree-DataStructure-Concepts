#Problem 404. Sum of Left Leaves

'''
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


#Approach: 
Traverse the tree using DFS, everytime a node is a left side, we will have a boolean check to make sure that the node is left-side, and them all together

#Time complexity: O(n), n is the number of node in the tree, the algorithm will have to travel through all node check for the valid sum
#Space complexity: O(n), n is the number of node in the tree, the program needs to save a space of O(n) as the recursion stack will run onto the nth node in the tree


'''
#Treenode definition: 
class TreeNode: 
	#tree constructor: 
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def sumOfLeftLeaves(root):
	#helper method to run through the tree using DFS recursively
	def dfs(root, isLeft):
		#the root node we are looking at is empty
		if not root: 
			return 0
		#return the left leaf node
		if not root.left and not root.right and isLeft: 
			return root.val
		#add the sum of all leaf node recursively
		return dfs(root.left, True) + dfs(root.right, False)

		
	return dfs(root, False)



#Main function to run the test case:
def main():
	print("TESTING SUM OF LEFT LEAVES...")
	#build the node: 

	root = TreeNode(3)
	nine = TreeNode(9)
	twenty = TreeNode(20)
	fifteen = TreeNode(15)
	seven = TreeNode(7)

	#build the tree:
	root.left = nine
	root.right = twenty
	twenty.left = fifteen
	twenty.right = seven
	print(sumOfLeftLeaves(root))
	print("END OF TESTING...")

main()
