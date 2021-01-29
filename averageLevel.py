#Problem 637. Average of Levels in Binary Tree


'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

'''
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None

def averageOfLevels(root):
	#base case: 
	if not root: 
		return []
	#a dictionary to store the node and its level number
	levels = defaultdict(list)
	#the queue to store each particular tree node
	queue = [(root, 1)]
	level = 0
	#if the queue still has tree node, we keep running the bfs algorithm 
	while queue: 
		node, level = queue.pop(0)
		levels[level].append(node.val)
		#check the left and right tree for its node, if they are equal to each other
		if node.left is not None:
			queue.append((node.left, level+1))
		if node.right is not None:
			queue.append((node.right, level+1))
	return [sum(levels[i]) / len(levels[i]) for i in range(1, level + 1)]


#Main function to run the test cases:
def main():
	print("TESTING AVERAGE LEVELS IN BINARY TREE...")
	root = TreeNode(3)
	second_left = TreeNode(9)
	second_right = TreeNode(20)
	root.left = second_left
	root.right = second_right
	third_left = TreeNode(15)
	third_right = TreeNode(7)
	second_right.left = third_left
	second_right.right = third_right
	print(averageOfLevels(root))
	print("END OF TESTING...")

main()
