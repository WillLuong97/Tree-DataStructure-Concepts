#Problem 783. Minimum Distance Between BST Nodes

'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
'''
#Definition of a binary tree
class TreeNode: 
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def minDiffInBST(root):
	nodeArr = []
	#helper method to run inorder traversal through the tree and find the difference
	def inorder(node):
		if node: 
			inorder(node.left)
			nodeArr.append(node.val)
			inorder(node.right)
	#append all value from the tree into an array and since the bst is traversed inorderly, this means that 
	#the list of node returned will be sorted
	inorder(root)
	
	#since the array is sorted, we will assume the smallest difference will be between the first two value in the array
	assumed_min = nodeArr[1] - nodeArr[0]
	
	#loop through the rest of the array to see if there can be any smaller difference
	for i in range(1, len(nodeArr)):
		curr_min = nodeArr[i] - nodeArr[i-1]
		assumed_min = min(assumed_min, curr_min)
	return assumed_min	



#Main function to run the test cases: 
def main():
	print("TESTING MINIMUM DISTANCE BETWEEN BST NODES...") 

	root = [4,2,6,1,3]
	print(minDiffInBST(root))

	root = [1,0,48,None,None,12,49]
	print(minDiffInBST(root))
	print("END OF TESTING...")

main()
