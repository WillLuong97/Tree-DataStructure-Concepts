#938. Range Sum of BST

'''
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
'''

class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    
#Pre-order approach:
#Time complexity: O(n), where N is the number of nodes in the tree
#Space complexity: O(n), where N is the number of recursion stack needed to be stored in the array
def rangeSumBST(root, low, high):
    #base case: 
    if not root: 
        return None
    result = 0
    #helper method to run through the tree using dfs:
    def dfs(root):
        if root: 
            #check if the root node is in the path or not
            if low <= root.val <= high: 
                result += root.val

            if low <= root.val:
                dfs(root.left)

            if root.val <= high:
                dfs(root.right) 
            

    dfs(root)
    return result


#main function: 
def main():
    print("TESTING RANGE SUM BST...")
    root_1 = [10,5,15,3,7,None,18]
    low_1 = 7
    high_1 = 15
    root_2 = [10,5,15,3,7,13,18,1,None,6]
    low_2 = 6
    high_2 = 10
    print(rangeSumBST(root_1, low_1, high_1))
    print(rangeSumBST(root_2, low_2, high_2))
    print("END OF TESTING")
main()