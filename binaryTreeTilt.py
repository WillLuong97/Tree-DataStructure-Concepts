#Binay Tree Tilt

'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Example 1: 
Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1

Example 2:
Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
Example 3:


Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

#Brain storming: 


=> Goals: Return the sum of all tilt in a binary tree. 
Tilt is the abs difference between the sum of all left sub tree vs the sum of all right sub tree. Tilt is recursively tree for all tree node!
If a node does not have a child left tree or child right tree, the values are equate to 0.

#Approach: Traverse the tree using Post-order travesal, calculate and keep track of the tilt value at each node, and then sum it all up.
The overall idea is that we traverse each node, and calculate the tilt value for each node. At the end, we sum up all the tilt values, which is the desired result of the problem.

'''
#Definion of a bianry tree:
class TreeNode:
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

def findTilt(root):
	#base case: 
	if not root: 
		return 0
	result = 0
	#helper method to run Post-order appproah on the tree and find the tilt value
	def postorder(node):
		nonlocal result
		if node: 
			leftSum = postorder(node.left)
			rightSum = postorder(node.right)
			# adding the tilt value from child node together
			result += abs(leftSum - rightSum)
			
			return leftSum + rightSum + node.val

		else: 
			return 0

	postorder(root)
	return result
'''
Time complexity: O(n), the algorithm have to traverse each node exactly once to calculate the tilt.
Space complexity: Although, the space for our variable is constant-size, our recursion stack has to run n times, to cover all the tree node. 
'''
#Main function to run the test cases: 
def main(): 
	print("TESTING BINARY TREE TILT...")
	root = [1,2,3]
	findTilt(root)
	root = [4,2,9,3,5,None,7] 
	findTilt(root)
	root = [21,7,14,1,1,2,2,3,3]
	findTilt(root)	
	print("END OF TESTING....")

main()
