# Leetcode 1022. Sum of Root To Leaf Binary Numbers

'''
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
Example 3:

Input: root = [1]
Output: 1
Example 4:

Input: root = [1,1]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
'''
#Tree node structure: 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def sumRootToLeaf(root):
	#variable init 
	stack = []
	result = 0
	#pass in the root and 0 onto the stack
	stack.append((root, 0))
	
	while stack: 
		root, current = stack.pop()
		#convert into the decimal value
		if root is not None: 
			current = (current << 1) | root.val
			#check if the current node is a leaf or not, if it is, then append it to
			if root.right is None and root.left is None: 
				result += current
			else:
				stack.append((root.left, current))
				stack.append((root.right, current))

	return result

'''
Time complexity: O(n), n is the number of node, where every node must be met at least once
Space complexity:  up to O(h) to keep the stack, where h is a tree height.
'''

def sumRootToLeaf_RECURSION(root):
	result = 0
	#helper method to traverse the tree recursively
	def helper(root, current):
		nonlocal result
		#check if the current root number is a leaf or not
		if root:
			current = (current << 1) | root.val
			if root.right is None and root.left is None: 
				result += current
			helper(root.right, current)
			helper(root.left, current)
	
	
	helper(root, 0)
	return result

'''
Time complexity:O(N), where n  is a number of nodes, since one has to visit each node.

Space complexity: up to O(H) to keep the recursion stack, where HH is a tree height.
'''

#Main function to run the test cases
def main():
	print("TESTING SUM OF ROOT TO LEAF BINARY NUMBER...")
	#instance of a root node: 
	root = TreeNode(1)
	root.left = TreeNode(1)
	root.right = TreeNode(0)
	root.left.left = TreeNode(0)
	root.left.right = TreeNode(1)
	print(sumRootToLeaf(root))		
	print(sumRootToLeaf_RECURSION(root))
	print("END OF TESTING...")
main()
