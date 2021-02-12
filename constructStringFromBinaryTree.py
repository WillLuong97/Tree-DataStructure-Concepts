#Problem 606. Construct String from Binary Tree
'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''
#Definition of a binary tree node
class TreeNode:
	#contructor
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def tree2str(t):
	#preroder traversal
	if t: 
		#converting the current tree node into a string
		strT = str(t.val)
		left = tree2str(t.left)
		right = tree2str(t.right)
		if not left and not right: 
			return strT
		#adding the parentheses based on the tree node value
		else:
			strT += "(" + left + ")"
			if right:
				strT += "(" + right + ")"
			return strT
	return ""

#Time complexity: O(n), n is the total number of all node in the tree, because we have to traverse through the whole tree and get each element
#Space complexity: O(n), the recursion stack will run until all tree node has been processed. 	
#Main function to run the test case: 
def main():
	print("TESTING CONSTRUCTING STRING FROM BINARY TREE...")

	root = TreeNode(1)
	two = TreeNode(2)
	three = TreeNode(3)
	four = TreeNode(4)
	root.left = two
	root.right = three
	two.left = four
	print(tree2str(root))

	print("END OF TESTING...")


main()






