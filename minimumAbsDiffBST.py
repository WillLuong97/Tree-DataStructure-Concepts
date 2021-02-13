#Problem 530. Minimum Absolute Difference in BST

'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
'''
#Definition of a Tree Node
class TreeNode: 
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

'''
Since the tree is a BST, we will traverse the tree using inorder traversal, which could give us a sorted array. Once we have a sorted array, we will just check the difference between each consecutive value.
Since the array is sorted, the difference between each value would increase as the difference between each number expands, i.e, 1,2 is lesser than 1,3.
'''
def getMinimumDifference(root):
	#Base case:
	if not root:
		return 0
	sorted_node_array = []
	#helper method to perform inorder traversal in the tree
	def inorder(node):
		if node:
			inorder(node.left)
			sorted_node_array.append(node.val)
			inorder(node.right)
	#ruin inorder traversal through the tree
	inorder(root)
	#we are assuming the smallest value in the sorted array is the difference between the first two value. 
	minimum_diff = sorted_node_array[1] - sorted_node_array[0]
	#loop through the rest of the sorted array to check for any difference that would be even smaller
	for i in range(1, len(sorted_node_array)):
		local_diff = sorted_node_array[i] - sorted_node_array[i-1]
		minimum_diff = min(minimum_diff, local_diff)


	return minimum_diff

#Time complexity: O(N), n is the number of all node in the tree since we have to traverse the tree using inorder traversal and looking at each node in the tree
#Space complexity:  O(n), we have to store a sorted array of all node in the array.
#Main function to run the test cases: 
def main():
	print("TESTING MINIMUM ABSOLUTE DIFFERENCE IN BST...")
	
	root = TreeNode(1)
	two = TreeNode(2)
	three = TreeNode(3)
	root.right = three
	three.left = two

	print(getMinimumDifference(root))

	print("END OF TESTING...")

main()
