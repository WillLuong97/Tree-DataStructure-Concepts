#Leetcode 257. Binary Tree Paths

'''
Problem statement: 
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''
#Solution: solve this problem using Preorder traversal DFS algorithm:
def binaryTreePaths(root):
    #base case: 
    if not root: 
        return []

    #variable to store the final solution: 
    result = []

    #helper method to run the inorder traversal on the tree
    def helper(root, temp):
        #base case:
        if not root:
            return 

        #if the current tree node exist, then we will run dfs through it and its child node: 
        if root: 
            if not root.left and not root.right:
                temp.append(str(root.val))
                result.append("->".join(temp))
            helper(root.left, temp+[str(root.val)])
            helper(root.right, temp+[str(root.val)])
    helper(root, [])
    return result