#Problem 653. Two Sum IV - Input is a BST

'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
'''    
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
#The approach is to traverse through the tree and add all of its node value into 1-d array and then we search for the two sum there.
#Since the tree is bst, when we do inorder approach, the array would be sorted
def findTarget(root, k):
	#helper method to copy each element from the tree
	def dfs(root, array):
		if root:
			dfs(root.left, array)
			array.append(root.val)
			dfs(root.right, array)
	node_array = []
	dfs(root, node_array)
	#setting up the 2 boundary to check for the two sum in the node_array
	left = 0
	right = len(node_array) - 1
	while left < right:
		#we use binary search to look for the sum
		curr_sum = node_array[left] + node_array[right]
		if curr_sum == k:
			return True
		if curr_sum < k:
			left += 1	
		else: 
			right -= 1
		
	return False

	
'''
Time complexity: O(n), n is the number of node in a tree.
Space complexity: O(n), n is the number of node in a tree, we need to store the node_array with every element in the tree. 
'''
#Main function to run the test cases:
def main():
	print("TESTING TWO SUM IV - INPUT IS A BST")
	root = TreeNode(5)
	root.left = TreeNode(3)
	root.left.left = TreeNode(2)
	root.left.right = TreeNode(4)
	root.right = TreeNode(6)
	root.right.right = TreeNode(7)
	k = 9
	print(findTarget(root, k))
	print("END OF TESTING...")

main()
